import json


def get_content(request, fp):
    with fp.open("r", encoding="utf-8") as src:
        con = src.read()
        return con


def load_json_file(self, fj):
    with fj.open("r") as j:
        return json.load(j)