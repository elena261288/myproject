def extract_path(self):  # выделяем из всего пути начало
    # path = self.path.split('/')[1]
    # path = path.split("?")[0]
    # return path.split("#")[0]
    path = self.path.split("?")[0]
    path, *_qs = path.split("#")[0]
    if path[-1] == "/":
        path = path[:-1]
    print(path)


def separation_header(self, method):
    handlers = {
        "hello": print("hello"),
        "goodbye": print("goodbye"),
        "skills": print("skills"),
        "education": print("education"),
        "/job": print("job"),
        "": print("hi"),
        # "/": self.handler_index
    }
    path = self.extract_path()
    if path is not handlers:
        raise Exception

    handler = handlers[path]
    try:
        handler(method)
    except Exception:
        print("what do u want?")
