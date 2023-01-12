from _typeshed import Incomplete, Self
from abc import abstractmethod
from typing_extensions import Literal, TypeAlias

from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.title import Title
from openpyxl.descriptors.base import _BoolSetter, _FloatSetter, _IntegerSetter
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.xml.functions import _Element

from .layout import Layout
from .shapes import GraphicalProperties
from .text import RichText, Text

_Unused: TypeAlias = object

class ChartLines(Serialisable):
    tagname: str
    spPr: GraphicalProperties | None
    graphicalProperties = spPr  # noqa: F821
    def __init__(self, spPr: GraphicalProperties | None = ...) -> None: ...

class Scaling(Serialisable):
    tagname: str
    @property
    def logBase(self) -> float | None: ...
    @logBase.setter
    def logBase(self, __value: _FloatSetter | None) -> None: ...
    orientation: Literal["maxMin", "minMax"]
    @property
    def max(self) -> float | None: ...
    @max.setter
    def max(self, __value: _FloatSetter | None) -> None: ...
    @property
    def min(self) -> float | None: ...
    @min.setter
    def min(self, __value: _FloatSetter | None) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        logBase: _FloatSetter | None = ...,
        orientation: Literal["maxMin", "minMax"] = ...,
        max: _FloatSetter | None = ...,
        min: _FloatSetter | None = ...,
        extLst: _Unused = ...,
    ) -> None: ...

class _BaseAxis(Serialisable):
    @property
    def axId(self) -> int: ...
    @axId.setter
    def axId(self, __value: _IntegerSetter) -> None: ...
    scaling: Scaling
    @property
    def delete(self) -> bool: ...
    @delete.setter
    def delete(self, __value: _BoolSetter) -> None: ...
    axPos: Literal["b", "l", "r", "t"]
    majorGridlines: ChartLines | None
    minorGridlines: ChartLines | None
    title: Title | None
    numFmt: NumFmt | None
    number_format = numFmt  # noqa: F821
    majorTickMark: Literal["cross", "in", "out", None]
    minorTickMark: Literal["cross", "in", "out", None]
    tickLblPos: Literal["high", "low", "nextTo", None]
    spPr: GraphicalProperties | None
    graphicalProperties = spPr  # noqa: F821
    txPr: RichText | None
    textProperties = txPr  # noqa: F821
    @property
    def crossAx(self) -> int: ...
    @crossAx.setter
    def crossAx(self, __value: _IntegerSetter) -> None: ...
    crosses: Literal["autoZero", "max", "min", None]
    @property
    def crossesAt(self) -> float | None: ...
    @crossesAt.setter
    def crossesAt(self, __value: _FloatSetter | None) -> None: ...
    __elements__: tuple[str, ...]
    def __init__(
        self,
        axId: _IntegerSetter,
        scaling: Scaling | None,
        delete: _BoolSetter,
        axPos: str,
        majorGridlines: ChartLines | None,
        minorGridlines: ChartLines | None,
        title: Title | None,
        numFmt: Incomplete | None,
        majorTickMark: Literal["cross", "in", "out", None],
        minorTickMark: Literal["cross", "in", "out", None],
        tickLblPos: Literal["high", "low", "nextTo", None],
        spPr: GraphicalProperties | None,
        txPr: RichText | None,
        crossAx: _IntegerSetter,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _FloatSetter | None = ...,
    ) -> None: ...
    @property
    @abstractmethod
    def tagname(self) -> str: ...

class DisplayUnitsLabel(Serialisable):
    tagname: str
    layout: Layout | None
    tx: Text | None
    text = tx  # noqa: F821
    spPr: GraphicalProperties | None
    graphicalProperties = spPr  # noqa: F821
    txPr: RichText | None
    textPropertes = txPr  # noqa: F821
    __elements__: tuple[str, ...]
    def __init__(
        self,
        layout: Layout | None = ...,
        tx: Text | None = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
    ) -> None: ...

class DisplayUnitsLabelList(Serialisable):
    tagname: str
    @property
    def custUnit(self) -> float | None: ...
    @custUnit.setter
    def custUnit(self, __value: _FloatSetter | None) -> None: ...
    builtInUnit: Literal[
        "hundreds",
        "thousands",
        "tenThousands",
        "hundredThousands",
        "millions",
        "tenMillions",
        "hundredMillions",
        "billions",
        "trillions",
        None,
    ]
    dispUnitsLbl: DisplayUnitsLabel | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        custUnit: float | None = ...,
        builtInUnit: Literal[
            "hundreds",
            "thousands",
            "tenThousands",
            "hundredThousands",
            "millions",
            "tenMillions",
            "hundredMillions",
            "billions",
            "trillions",
            None,
        ] = ...,
        dispUnitsLbl: DisplayUnitsLabel | None = ...,
        extLst: _Unused = ...,
    ) -> None: ...

class NumericAxis(_BaseAxis):
    tagname: str
    crossBetween: Literal["between", "midCat", None]
    @property
    def majorUnit(self) -> float | None: ...
    @majorUnit.setter
    def majorUnit(self, __value: _FloatSetter | None) -> None: ...
    @property
    def minorUnit(self) -> float | None: ...
    @minorUnit.setter
    def minorUnit(self, __value: _FloatSetter | None) -> None: ...
    dispUnits: DisplayUnitsLabelList | None
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        crossBetween: Literal["between", "midCat", None] = ...,
        majorUnit: _FloatSetter | None = ...,
        minorUnit: _FloatSetter | None = ...,
        dispUnits: DisplayUnitsLabelList | None = ...,
        extLst: _Unused = ...,
        axId: _IntegerSetter = ...,
        scaling: Scaling | None = ...,
        delete: _BoolSetter = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _IntegerSetter = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _FloatSetter | None = ...,
    ) -> None: ...
    @classmethod
    def from_tree(cls: Self, node: _Element) -> Self: ...

class TextAxis(_BaseAxis):
    tagname: str
    @property
    def auto(self) -> bool | None: ...
    @auto.setter
    def auto(self, __value: _BoolSetter) -> None: ...
    lblAlgn: Literal["ctr", "l", "r", None]
    @property
    def lblOffset(self) -> float: ...
    @lblOffset.setter
    def lblOffset(self, __value: _FloatSetter) -> None: ...
    @property
    def tickLblSkip(self) -> int | None: ...
    @tickLblSkip.setter
    def tickLblSkip(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def tickMarkSkip(self) -> int | None: ...
    @tickMarkSkip.setter
    def tickMarkSkip(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def noMultiLvlLbl(self) -> bool | None: ...
    @noMultiLvlLbl.setter
    def noMultiLvlLbl(self, __value: _BoolSetter) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        auto: _BoolSetter = ...,
        lblAlgn: Literal["ctr", "l", "r", None] = ...,
        lblOffset: _FloatSetter = ...,
        tickLblSkip: _IntegerSetter | None = ...,
        tickMarkSkip: _IntegerSetter | None = ...,
        noMultiLvlLbl: _BoolSetter = ...,
        extLst: _Unused = ...,
        axId: _IntegerSetter = ...,
        scaling: Scaling | None = ...,
        delete: _BoolSetter = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _IntegerSetter = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _FloatSetter | None = ...,
    ) -> None: ...

class DateAxis(TextAxis):
    tagname: str
    @property
    def auto(self) -> bool | None: ...
    @auto.setter
    def auto(self, __value: _BoolSetter) -> None: ...
    @property  # type: ignore[override]
    def lblOffset(self) -> int | None: ...
    @lblOffset.setter
    def lblOffset(self, __value: _IntegerSetter | None) -> None: ...
    baseTimeUnit: Literal["days", "months", "years", None]
    @property
    def majorUnit(self) -> float | None: ...
    @majorUnit.setter
    def majorUnit(self, __value: _FloatSetter | None) -> None: ...
    majorTimeUnit: Literal["days", "months", "years", None]
    @property
    def minorUnit(self) -> float | None: ...
    @minorUnit.setter
    def minorUnit(self, __value: _FloatSetter | None) -> None: ...
    minorTimeUnit: Literal["days", "months", "years", None]
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        auto: _BoolSetter = ...,
        lblOffset: _IntegerSetter | None = ...,
        baseTimeUnit: Literal["days", "months", "years", None] = ...,
        majorUnit: _FloatSetter | None = ...,
        majorTimeUnit: Literal["days", "months", "years", None] = ...,
        minorUnit: _FloatSetter | None = ...,
        minorTimeUnit: Literal["days", "months", "years", None] = ...,
        extLst: ExtensionList | None = ...,
        axId: _IntegerSetter = ...,
        scaling: Scaling | None = ...,
        delete: _BoolSetter = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _IntegerSetter = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _FloatSetter | None = ...,
    ) -> None: ...

class SeriesAxis(_BaseAxis):
    tagname: str
    @property
    def tickLblSkip(self) -> int | None: ...
    @tickLblSkip.setter
    def tickLblSkip(self, __value: _IntegerSetter | None) -> None: ...
    @property
    def tickMarkSkip(self) -> int | None: ...
    @tickMarkSkip.setter
    def tickMarkSkip(self, __value: _IntegerSetter | None) -> None: ...
    extLst: ExtensionList | None
    __elements__: tuple[str, ...]
    def __init__(
        self,
        tickLblSkip: _IntegerSetter | None = ...,
        tickMarkSkip: _IntegerSetter | None = ...,
        extLst: _Unused = ...,
        axId: _IntegerSetter = ...,
        scaling: Scaling | None = ...,
        delete: _BoolSetter = ...,
        axPos: str = ...,
        majorGridlines: ChartLines | None = ...,
        minorGridlines: ChartLines | None = ...,
        title: Title | None = ...,
        numFmt: Incomplete | None = ...,
        majorTickMark: Literal["cross", "in", "out", None] = ...,
        minorTickMark: Literal["cross", "in", "out", None] = ...,
        tickLblPos: Literal["high", "low", "nextTo", None] = ...,
        spPr: GraphicalProperties | None = ...,
        txPr: RichText | None = ...,
        crossAx: _IntegerSetter = ...,
        crosses: Literal["autoZero", "max", "min", None] = ...,
        crossesAt: _FloatSetter | None = ...,
    ) -> None: ...
