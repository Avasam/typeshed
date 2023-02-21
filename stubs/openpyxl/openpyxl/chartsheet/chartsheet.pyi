from _typeshed import Incomplete
from typing_extensions import Literal

from openpyxl import _Decodable
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.workbook.child import _WorkbookChild

class Chartsheet(_WorkbookChild, Serialisable):
    tagname: str
    mime_type: str
    sheetPr: Incomplete
    sheetViews: Incomplete
    sheetProtection: Incomplete
    customSheetViews: Incomplete
    pageMargins: Incomplete
    pageSetup: Incomplete
    drawing: Incomplete
    drawingHF: Incomplete
    picture: Incomplete
    webPublishItems: Incomplete
    extLst: Incomplete
    sheet_state: Literal["visible", "hidden", "veryHidden"]
    headerFooter: Incomplete
    HeaderFooter: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        sheetPr: Incomplete | None = ...,
        sheetViews: Incomplete | None = ...,
        sheetProtection: Incomplete | None = ...,
        customSheetViews: Incomplete | None = ...,
        pageMargins: Incomplete | None = ...,
        pageSetup: Incomplete | None = ...,
        headerFooter: Incomplete | None = ...,
        drawing: Incomplete | None = ...,
        drawingHF: Incomplete | None = ...,
        picture: Incomplete | None = ...,
        webPublishItems: Incomplete | None = ...,
        extLst: Incomplete | None = ...,
        parent: Incomplete | None = ...,
        title: str | _Decodable = ...,
        sheet_state: Literal["visible", "hidden", "veryHidden"] = ...,
    ) -> None: ...
    def add_chart(self, chart) -> None: ...
    def to_tree(self): ...
