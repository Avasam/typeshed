from _typeshed import Incomplete
from collections.abc import Iterator
from typing import Generic, TypeVar, overload
from typing_extensions import Literal

from networkx.classes.graph import Edge, Graph, NBunch, _Node

_D = TypeVar("_D")
_U = TypeVar("_U")

class NodeView(Generic[_Node]):
    def __init__(self, graph: Graph[_Node]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_Node]: ...
    def __getitem__(self, n: _Node) -> _Node: ...
    def __contains__(self, n: object) -> bool: ...
    @overload
    def __call__(self, data: Literal[False] = False, default=None) -> NodeView[_Node]: ...
    @overload
    def __call__(self, data: Literal[True] | str, default=None) -> NodeDataView[_Node]: ...
    def data(self, data: bool | str = True, default=None) -> NodeDataView[_Node]: ...

class NodeDataView(Generic[_Node]):
    def __init__(self, nodedict: dict[str, Incomplete], data: bool | str = False, default=None) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[_Node, Incomplete]]: ...
    def __contains__(self, n: _Node) -> bool: ...
    def __getitem__(self, n: _Node): ...

class DiDegreeView(Generic[_Node]):
    def __init__(self, G: Graph[_Node], nbunch: NBunch[_Node] = None, weight: None | bool | str = None) -> None: ...
    def __call__(self, nbunch: NBunch[_Node] = None, weight: None | bool | str = None) -> DiDegreeView[_Node]: ...
    def __getitem__(self, n: _Node) -> float: ...
    def __iter__(self) -> Iterator[tuple[_Node, float]]: ...
    def __len__(self) -> int: ...

class DegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class OutDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class InDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class MultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class DiMultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class InMultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...
class OutMultiDegreeView(DiDegreeView[_Node], Generic[_Node]): ...

class OutEdgeDataView(Generic[_Node, _D]):
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_D]: ...
    def __contains__(self, e: Edge[_Node]) -> bool: ...

class EdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...
class InEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...
class OutMultiEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...
class MultiEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...
class InMultiEdgeDataView(OutEdgeDataView[_Node, _D], Generic[_Node, _D]): ...

class OutEdgeView(Generic[_Node]):
    def __init__(self, graph: Graph[_Node]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[_Node, _Node]]: ...
    def __contains__(self, e: Edge[_Node]) -> bool: ...
    def __getitem__(self, e: Edge[_Node]) -> dict[str, Incomplete]: ...
    @overload
    def __call__(self, nbunch: NBunch[_Node] = None, data: Literal[False] = False, default=None) -> OutEdgeView[_Node]: ...
    @overload
    def __call__(
        self, *, nbunch: NBunch[_Node] = None, data: Literal[True], default=None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: NBunch[_Node] = ..., data: str = ..., default: _U = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(self, data: Literal[False] = False, default=None, nbunch: NBunch[_Node] = None) -> OutEdgeView[_Node]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default=None, nbunch: NBunch[_Node] = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: str = ..., default: _U = None, nbunch: NBunch[_Node] = ...
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...

class EdgeView(OutEdgeView[_Node], Generic[_Node]): ...
class InEdgeView(OutEdgeView[_Node], Generic[_Node]): ...
class OutMultiEdgeView(OutEdgeView[_Node], Generic[_Node]): ...
class MultiEdgeView(OutMultiEdgeView[_Node], Generic[_Node]): ...
class InMultiEdgeView(OutMultiEdgeView[_Node], Generic[_Node]): ...
