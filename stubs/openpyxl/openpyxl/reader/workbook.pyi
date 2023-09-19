from _typeshed import Incomplete
from collections.abc import Generator, Iterable

from openpyxl.packaging.relationship import Relationship, RelationshipList
from openpyxl.packaging.workbook import ChildSheet, PivotCache
from openpyxl.pivot.cache import CacheDefinition
from openpyxl.workbook import Workbook

class WorkbookParser:
    archive: Incomplete
    workbook_part_name: str
    wb: Workbook
    keep_links: bool
    sheets: list[ChildSheet]
    def __init__(self, archive, workbook_part_name: str, keep_links: bool = True) -> None: ...
    @property
    def rels(self) -> RelationshipList: ...
    caches: Iterable[PivotCache]
    def parse(self) -> None: ...
    def find_sheets(self) -> Generator[tuple[ChildSheet, Relationship], None, None]: ...
    def assign_names(self) -> None: ...
    @property
    def pivot_caches(self) -> dict[int, CacheDefinition]: ...
