from urllib.parse import parse_qs


def load_user_session(request):
    session = request.session
    if not session or session.is_empty():
        return {}
    return session


def build_query_args(request):
    #_path, *qs = path.split("?")
    #args = {}

    #if len(qs) != 1:
    #    return args

    #qs = qs[0]
    #qs = parse_qs(qs)
    qs = request.GET
    if not qs:
        return {}

    args = {}

    for key, values in qs.items():
        if not values:
            continue
        value = values
        if isinstance(values, list):
            value = values[0]

        args[key] = value
    return args


def build_name(query_args):
    return query_args.get("name", "friend")


def build_age(query_args):
    return query_args.get("age")
