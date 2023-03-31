import datetime
from decimal import Decimal
from re import Pattern
from typing import overload
from typing_extensions import Final, Literal, TypeAlias

from openpyxl.cell.rich_text import CellRichText
from openpyxl.comments.comments import Comment
from openpyxl.compat.numbers import NUMERIC_TYPES as NUMERIC_TYPES
from openpyxl.styles.cell_style import StyleArray
from openpyxl.styles.styleable import StyleableObject
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.worksheet.formula import ArrayFormula, DataTableFormula
from openpyxl.worksheet.hyperlink import Hyperlink

_TimeTypes: TypeAlias = datetime.datetime | datetime.date | datetime.time | datetime.timedelta
_CellValue: TypeAlias = (  # if numpy is installed also numpy bool and number types
    bool | float | Decimal | str | CellRichText | _TimeTypes | DataTableFormula | ArrayFormula
)

TIME_TYPES: tuple[type, ...]
TIME_FORMATS: dict[type[_TimeTypes], str]
STRING_TYPES: tuple[type, ...]
KNOWN_TYPES: tuple[type, ...]

ILLEGAL_CHARACTERS_RE: Pattern[str]
ERROR_CODES: Final[tuple[str, ...]]

TYPE_STRING: Final = "s"
TYPE_FORMULA: Final = "f"
TYPE_NUMERIC: Final = "n"
TYPE_BOOL: Final = "b"
TYPE_NULL: Final = "n"
TYPE_INLINE: Final = "inlineStr"
TYPE_ERROR: Final = "e"
TYPE_FORMULA_CACHE_STRING: Final = "str"

VALID_TYPES: Final[tuple[str, ...]]

def get_type(t: type, value: object) -> Literal["n", "s", "d", "f", None]: ...
def get_time_format(t: _TimeTypes) -> str: ...

class Cell(StyleableObject):
    row: int | None
    column: int | None
    data_type: str
    def __init__(
        self,
        worksheet: _WorkbookChild,
        row: int | None = None,
        column: int | None = None,
        value: _CellValue | bytes | None = None,
        style_array: StyleArray | None = None,
    ) -> None: ...
    @property
    def coordinate(self) -> str: ...
    @property
    def col_idx(self) -> int: ...
    @property
    def column_letter(self) -> str: ...
    @property
    def encoding(self) -> str: ...
    @property
    def base_date(self) -> datetime.datetime: ...
    @overload
    def check_string(self, value: None) -> None: ...
    @overload
    def check_string(self, value: str | bytes) -> str: ...
    def check_error(self, value: object) -> str: ...
    @property
    def value(self) -> _CellValue: ...
    @value.setter
    def value(self, value: _CellValue | bytes | None) -> None: ...
    @property
    def internal_value(self) -> _CellValue: ...
    @property
    def hyperlink(self) -> Hyperlink | None: ...
    @hyperlink.setter
    def hyperlink(self, val: Hyperlink | str | None) -> None: ...
    @property
    def is_date(self) -> bool: ...
    def offset(self, row: int = 0, column: int = 0) -> Cell: ...
    @property
    def comment(self) -> Comment | None: ...
    @comment.setter
    def comment(self, value: Comment | None) -> None: ...

class MergedCell(StyleableObject):
    data_type: str
    comment: Comment | None
    hyperlink: Hyperlink | None
    row: int | None
    column: int | None
    def __init__(self, worksheet: _WorkbookChild, row: int | None = None, column: int | None = None) -> None: ...
    @property
    def coordinate(self) -> str: ...
    value: _CellValue | bytes | None

def WriteOnlyCell(ws: _WorkbookChild | None = None, value: _CellValue | bytes | None = None) -> Cell: ...
