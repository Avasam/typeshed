from typing import ClassVar

from openpyxl.descriptors.excel import Relation
from openpyxl.descriptors.serialisable import Serialisable

class ExternalReference(Serialisable):
    tagname: ClassVar[str]
    id: Relation
    def __init__(self, id: str | None) -> None: ...
