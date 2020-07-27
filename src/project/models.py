import json
import os
from dataclasses import dataclass, asdict
from datetime import date, datetime
from typing import Callable

from django.conf import settings


class ModelError(Exception):
    pass


@dataclass
class Model:
    __dataclass_fields__ = None
    pk = None

    __json_file__ = None

    @classmethod
    def all(cls):
        return tuple(cls._build_objects())

    @classmethod
    def one(cls, object_id):
        try:
            obj = next(cls._build_objects(lambda record: record[0] == object_id))
        except StopIteration:
            obj = None

        return obj

    def save(self):
        self._setup_pk()

        content = self._load_content()
        dct = asdict(self)

        try:
            del dct["pk"]
        except KeyError:
            pass

        content[self.pk] = dct
        self._store_content(content)

    def delete(self):
        content = self._load_content()

        if self.pk not in content:
            return

        del content[self.pk]
        self._store_content(content)

        self.pk = None

    @classmethod
    def source(cls):
        if not cls.__json_file__:
            raise TypeError(f"unbound source for {cls}")
        src = settings.REPO_DIR / "storage"/cls.__json_file__
        src = src.resolve()
        return src

    def _setup_pk(self):
        if self.pk:
            return

        self.pk = os.urandom(16).hex()


    @classmethod
    def _build_objects(cls, predicate: Callable = lambda _x: 1):
         content = cls._load_content()

         result = (cls(**kw) for kw in cls._build_kws(content, predicate))

         yield from result

    @ classmethod
    def _build_kws(cls, content, predicate = lambda _x: 1):
        for object_id, fields in filter(predicate, content.items()):
            kw = {}
            for field, field_params in cls.__dataclass_fields__.items():
                value = fields.get(field)
                value = cls._build_value(value, field_params.type)
                kw[field] = value
            kw["pk"] = object_id
            yield kw

    @classmethod
    def _load_content(cls):
        try:
            with cls.source().open("r") as src:
                payload = src.read()
                if not payload:
                    content = {}
                else:
                    content = json.loads(payload)

        except json.JSONDecodeError as err:
            raise ModelError("corrupted source") from err

        except FileNotFoundError:
            content = {}

        return content

    @classmethod
    def _store_content(cls, content):
        cleaned_content = cls._clean_content(content)
        with cls.source().open("w") as dst:
            json.dump(cleaned_content, dst)

    @classmethod
    def _validate_fields(cls, kwargs):
        updated_set = set(kwargs)
        allowed_set = set(cls.__dataclass_fields__)
        diff = updated_set - allowed_set
        if diff:
            raise ValueError(f"fields {sorted(diff)} are not supported by {cls}")

    @classmethod
    def _clean_content(cls, content):
        result = {}

        for key, value in content.items():
            if isinstance(value, (date, datetime)):
                value = value.strftime("%Y-%m-%d")
            elif isinstance(value, dict):
                value = cls._clean_content(value)
            result[key] = value

        return result

    @classmethod
    def _build_value(cls,value, field_type):
        if issubclass(date, field_type.__args__):
            return datetime.strptime(value, "%Y-%m-%d").date()
        return value














