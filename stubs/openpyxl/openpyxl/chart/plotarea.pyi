from _typeshed import Incomplete, Unused
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from openpyxl.chart.area_chart import AreaChart, AreaChart3D
from openpyxl.chart.axis import DateAxis, NumericAxis, SeriesAxis, TextAxis
from openpyxl.chart.bar_chart import BarChart, BarChart3D
from openpyxl.chart.bubble_chart import BubbleChart
from openpyxl.chart.layout import Layout
from openpyxl.chart.line_chart import LineChart, LineChart3D
from openpyxl.chart.pie_chart import DoughnutChart, PieChart, PieChart3D, ProjectedPieChart
from openpyxl.chart.radar_chart import RadarChart
from openpyxl.chart.scatter_chart import ScatterChart
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.stock_chart import StockChart
from openpyxl.chart.surface_chart import SurfaceChart, SurfaceChart3D
from openpyxl.chart.text import RichText
from openpyxl.descriptors.base import Alias, Typed, _ConvertibleToBool
from openpyxl.descriptors.excel import ExtensionList
from openpyxl.descriptors.nested import NestedBool, _HasTagAndGet
from openpyxl.descriptors.sequence import MultiSequence, MultiSequencePart, _SequenceParam
from openpyxl.descriptors.serialisable import Serialisable

_PlotAreaCharts: TypeAlias = (
    AreaChart
    | AreaChart3D
    | LineChart
    | LineChart3D
    | StockChart
    | RadarChart
    | ScatterChart
    | PieChart
    | PieChart3D
    | DoughnutChart
    | BarChart
    | BarChart3D
    | ProjectedPieChart
    | SurfaceChart
    | SurfaceChart3D
    | BubbleChart
)

_PlotAreaAxes: TypeAlias = NumericAxis | TextAxis | DateAxis | SeriesAxis

class DataTable(Serialisable):
    tagname: ClassVar[str]
    showHorzBorder: NestedBool[Literal[True]]
    showVertBorder: NestedBool[Literal[True]]
    showOutline: NestedBool[Literal[True]]
    showKeys: NestedBool[Literal[True]]
    spPr: Typed[GraphicalProperties, Literal[True]]
    graphicalProperties: Alias
    txPr: Typed[RichText, Literal[True]]
    extLst: Typed[ExtensionList, Literal[True]]
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(
        self,
        showHorzBorder: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showVertBorder: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showOutline: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        showKeys: _HasTagAndGet[_ConvertibleToBool | None] | _ConvertibleToBool | None = None,
        spPr: GraphicalProperties | None = None,
        txPr: RichText | None = None,
        extLst: Unused = None,
    ) -> None: ...

class PlotArea(Serialisable):
    tagname: ClassVar[str]
    layout: Typed[Layout, Literal[True]]
    dTable: Typed[DataTable, Literal[True]]
    spPr: Typed[GraphicalProperties, Literal[True]]
    graphicalProperties: Alias
    extLst: Typed[ExtensionList, Literal[True]]
    _charts: MultiSequence[_PlotAreaCharts]
    areaChart: MultiSequencePart[AreaChart]
    area3DChart: MultiSequencePart[AreaChart3D]
    lineChart: MultiSequencePart[LineChart]
    line3DChart: MultiSequencePart[LineChart3D]
    stockChart: MultiSequencePart[StockChart]
    radarChart: MultiSequencePart[RadarChart]
    scatterChart: MultiSequencePart[ScatterChart]
    pieChart: MultiSequencePart[PieChart]
    pie3DChart: MultiSequencePart[PieChart3D]
    doughnutChart: MultiSequencePart[DoughnutChart]
    barChart: MultiSequencePart[BarChart]
    bar3DChart: MultiSequencePart[BarChart3D]
    ofPieChart: MultiSequencePart[ProjectedPieChart]
    surfaceChart: MultiSequencePart[SurfaceChart]
    surface3DChart: MultiSequencePart[SurfaceChart3D]
    bubbleChart: MultiSequencePart[BubbleChart]
    _axes: MultiSequence[_PlotAreaAxes]
    valAx: NumericAxis
    catAx: TextAxis
    dateAx: DateAxis
    serAx: SeriesAxis
    __elements__: ClassVar[tuple[str, ...]]
    def __init__(
        self,
        layout: Layout | None = None,
        dTable: DataTable | None = None,
        spPr: GraphicalProperties | None = None,
        _charts: _SequenceParam[_PlotAreaCharts] = (),
        _axes: _SequenceParam[_PlotAreaAxes] = (),
        extLst: Unused = None,
    ) -> None: ...
    def to_tree(self, tagname: str | None = None, idx: Incomplete | None = None, namespace: str | None = None): ...
    @classmethod
    def from_tree(cls, node): ...
