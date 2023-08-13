from _typeshed import Incomplete

def generate_adjlist(G, delimiter: str = " ") -> None: ...
def write_adjlist(G, path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8") -> None: ...
def parse_adjlist(
    lines,
    comments: str = "#",
    delimiter: Incomplete | None = None,
    create_using: Incomplete | None = None,
    nodetype: Incomplete | None = None,
): ...
def read_adjlist(
    path,
    comments: str = "#",
    delimiter: Incomplete | None = None,
    create_using: Incomplete | None = None,
    nodetype: Incomplete | None = None,
    encoding: str = "utf-8",
): ...
