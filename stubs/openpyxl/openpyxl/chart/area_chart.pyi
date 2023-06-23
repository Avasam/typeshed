from _typeshed import Incomplete, Unused
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from openpyxl.chart.axis import ChartLines, NumericAxis, SeriesAxis, TextAxis
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.series import Series
from openpyxl.descriptors.base import Alias, Typed, _ConvertibleToBool, _ConvertibleToInt
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.nested import NestedBool, NestedSet, _HasTagAndGet
from openpyxl.descriptors.sequence import Sequence, _SequenceParam

from ._chart import ChartBase

_AreaChartBaseGrouping: TypeAlias = Literal["percentStacked", "standard", "stacked"]

class _AreaChartBase(ChartBase):
    grouping: NestedSet[_AreaChartBaseGrouping]
    varyColors: NestedBool[Literal[True]]
    ser: Sequence[Series, Literal[True], Literal[False]]
    dLbls: Typed[DataLabelList, Literal[True]]
    dataLabels: Alias
    dropLines: Typed[ChartLines, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(
        self,
        grouping: _HasTagAndGet[_AreaChartBaseGrouping] | _AreaChartBaseGrouping = "standard",
        varyColors: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        ser: _SequenceParam[Series | _HasTagAndGet[_ConvertibleToInt] | _ConvertibleToInt | None] = (),
        dLbls: DataLabelList | None = None,
        dropLines: ChartLines | None = None,
    ) -> None: ...

class AreaChart(_AreaChartBase):
    tagname: ClassVar[str]
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    x_axis: Typed[TextAxis, Literal[False]]
    y_axis: Typed[NumericAxis, Literal[False]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(self, axId: Unused = None, extLst: Unused = None, **kw) -> None: ...

class AreaChart3D(AreaChart):
    tagname: ClassVar[str]
    grouping: Incomplete
    varyColors: Incomplete
    ser: Incomplete
    dLbls: Incomplete
    dropLines: Incomplete
    gapDepth: Incomplete
    x_axis: Typed[TextAxis, Literal[False]]
    y_axis: Typed[NumericAxis, Literal[False]]
    z_axis: Typed[SeriesAxis, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(self, gapDepth: Incomplete | None = None, **kw) -> None: ...
