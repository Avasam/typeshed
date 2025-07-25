from openpyxl import _Decodable
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

class WriteOnlyWorksheet(_WorkbookChild):
    mime_type = Worksheet.mime_type
    add_chart = Worksheet.add_chart
    add_image = Worksheet.add_image
    add_table = Worksheet.add_table
    tables = Worksheet.tables
    print_titles = Worksheet.print_titles
    print_title_cols = Worksheet.print_title_cols
    print_title_rows = Worksheet.print_title_rows
    freeze_panes = Worksheet.freeze_panes
    print_area = Worksheet.print_area
    sheet_view = Worksheet.sheet_view
    def __init__(self, parent: Workbook | None, title: str | _Decodable | None) -> None: ...
    @property
    def closed(self) -> bool: ...
    def close(self) -> None: ...
    def append(self, row) -> None: ...
