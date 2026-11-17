"""HTTP routing helpers, unrelated to sequence routing research."""

ROUTES = {}


def route(pattern):
    def register(fn):
        ROUTES[pattern] = fn
        return fn
    return register


def dispatch(path, *args, **kwargs):
    for pattern, fn in ROUTES.items():
        if path.startswith(pattern):
            return fn(*args, **kwargs)
    raise KeyError(path)
