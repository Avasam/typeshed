from _typeshed import SupportsGetItem

from openpyxl import _VisibilityType
from openpyxl.utils.cell import _RangeBoundariesTuple
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

def read_dimension(source) -> _RangeBoundariesTuple | None: ...

class ReadOnlyWorksheet:
    cell = Worksheet.cell
    iter_rows = Worksheet.iter_rows
    values = Worksheet.values
    rows = Worksheet.rows
    __getitem__ = Worksheet.__getitem__
    __iter__ = Worksheet.__iter__
    parent: Workbook
    title: str
    sheet_state: _VisibilityType
    def __init__(
        self, parent_workbook: Workbook, title: str, worksheet_path, shared_strings: SupportsGetItem[int, str]
    ) -> None: ...
    def calculate_dimension(self, force: bool = False): ...
    def reset_dimensions(self) -> None: ...
    @property
    def min_row(self) -> int: ...
    @property
    def max_row(self) -> int | None: ...
    @property
    def min_column(self) -> int: ...
    @property
    def max_column(self) -> int | None: ...
