from _typeshed import Incomplete, Unused

from openpyxl.descriptors.serialisable import Serialisable

class Related(Serialisable):
    id: Incomplete
    def __init__(self, id: Incomplete | None = None) -> None: ...
    def to_tree(self, tagname: str | None, idx: Unused = None): ...  # type: ignore[override]
