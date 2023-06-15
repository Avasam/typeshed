from _typeshed import Incomplete, Unused
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.text import RichText
from openpyxl.descriptors.base import Alias, Typed, _ConvertibleToBool, _ConvertibleToInt
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.nested import NestedBool, NestedInteger, NestedNoneSet, NestedString, _HasTagAndGet, _NestedNoneSetParam
from openpyxl.descriptors.serialisable import Serialisable

_DataLabelBaseDLblPos: TypeAlias = Literal["bestFit", "b", "ctr", "inBase", "inEnd", "l", "outEnd", "r", "t"]

class _DataLabelBase(Serialisable):
    numFmt: NestedString[Literal[True]]
    spPr: Typed[GraphicalProperties, Literal[True]]
    graphicalProperties: Alias
    txPr: Typed[RichText, Literal[True]]
    textProperties: Alias
    dLblPos: NestedNoneSet[_DataLabelBaseDLblPos]
    position: Alias
    showLegendKey: NestedBool[Literal[True]]
    showVal: NestedBool[Literal[True]]
    showCatName: NestedBool[Literal[True]]
    showSerName: NestedBool[Literal[True]]
    showPercent: NestedBool[Literal[True]]
    showBubbleSize: NestedBool[Literal[True]]
    showLeaderLines: NestedBool[Literal[True]]
    separator: NestedString[Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(
        self,
        numFmt: object = None,
        spPr: GraphicalProperties | None = None,
        txPr: RichText | None = None,
        dLblPos: _NestedNoneSetParam[_DataLabelBaseDLblPos] = None,
        showLegendKey: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showVal: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showCatName: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showSerName: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showPercent: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showBubbleSize: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showLeaderLines: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        separator: object = None,
        extLst: Unused = None,
    ) -> None: ...

class DataLabel(_DataLabelBase):
    tagname: ClassVar[str]
    idx: NestedInteger[Literal[False]]
    numFmt: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(self, idx: _HasTagAndGet[_ConvertibleToInt] | _ConvertibleToInt = 0, **kw) -> None: ...

class DataLabelList(_DataLabelBase):
    tagname: ClassVar[str]
    dLbl: Incomplete
    delete: NestedBool[Literal[True]]
    numFmt: Incomplete
    spPr: Incomplete
    txPr: Incomplete
    dLblPos: Incomplete
    showLegendKey: Incomplete
    showVal: Incomplete
    showCatName: Incomplete
    showSerName: Incomplete
    showPercent: Incomplete
    showBubbleSize: Incomplete
    showLeaderLines: Incomplete
    separator: Incomplete
    extLst: Incomplete
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(
        self, dLbl=(), delete: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None, **kw
    ) -> None: ...
