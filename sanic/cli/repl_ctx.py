from typing import Any, NamedTuple


class REPLLocal(NamedTuple):
    var: Any
    name: str
    desc: str


class REPLContext:
    def __init__(self):
        self._locals: set[REPLLocal] = set()

    def add_local(self, var, name=None, desc=None):
        self._locals.add(
            REPLLocal(
                var,
                name or var.__name__,
                desc or _truncate(var.__doc__),
            )
        )


def _truncate(s, limit = 40):
    return s[:limit] + "..." if len(s) > limit else s
