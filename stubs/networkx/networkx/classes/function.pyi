from _typeshed import Incomplete
from collections.abc import Iterable
from typing import TypeVar, overload
from typing_extensions import Literal

from networkx.classes.graph import Graph

_T = TypeVar("_T")
_U = TypeVar("_U")

def nodes(G): ...
def edges(G, nbunch: Incomplete | None = None): ...
def degree(G, nbunch: Incomplete | None = None, weight: Incomplete | None = None): ...
def neighbors(G, n): ...
def number_of_nodes(G): ...
def number_of_edges(G): ...
def density(G): ...
def degree_histogram(G): ...
def is_directed(G): ...
def freeze(G): ...
def is_frozen(G): ...
def add_star(G_to_add_to, nodes_for_star, **attr) -> None: ...
def add_path(G_to_add_to, nodes_for_path, **attr) -> None: ...
def add_cycle(G_to_add_to, nodes_for_cycle, **attr) -> None: ...
def subgraph(G, nbunch): ...
def induced_subgraph(G: Graph[_T], nbunch: _T | Iterable[_T] | None) -> Graph[_T]: ...
def edge_subgraph(G, edges): ...
def restricted_view(G, nodes, edges): ...
def reverse_view(digraph): ...
def to_directed(graph): ...
def to_undirected(graph): ...
def create_empty_copy(G, with_data: bool = True): ...
def info(G, n: Incomplete | None = ...): ...
@overload
def set_node_attributes(G: Graph[_T], values: dict[_T, Incomplete], name: str = ...) -> None: ...

# Can "Incomplete scalar value" be enforced?
@overload
def set_node_attributes(G: Graph[Incomplete], values, name: str = ...) -> None: ...
@overload
def set_node_attributes(G: Graph[_T], values: dict[_T, dict[Incomplete, Incomplete]], name: None = None) -> None: ...
def get_node_attributes(G: Graph[_T], name: str) -> dict[_T, Incomplete]: ...
@overload
def set_edge_attributes(G: Graph[_T], values: dict[tuple[_T, _T], Incomplete], name: str = ...) -> None: ...
@overload
def set_edge_attributes(G: Graph[Incomplete], values, name: None = None) -> None: ...
def get_edge_attributes(G: Graph[_T], name: str) -> dict[tuple[_T, _T], Incomplete]: ...
def all_neighbors(graph: Graph[_T], node: _T) -> Iterable[_T]: ...
def non_neighbors(graph: Graph[_T], node: _T) -> Iterable[_T]: ...
def non_edges(graph: Graph[_T]) -> Iterable[tuple[_T, _T]]: ...
def common_neighbors(G: Graph[_T], u: _T, v: _T) -> Iterable[_T]: ...
def is_weighted(G: Graph[_T], edge: tuple[_T, _T] | None = None, weight: str | None = "weight") -> bool: ...
def is_negatively_weighted(G: Graph[_T], edge: tuple[_T, _T] | None = None, weight: str | None = "weight"): ...
def is_empty(G: Graph[Incomplete]) -> bool: ...
def nodes_with_selfloops(G: Graph[_T]) -> Iterable[_T]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[False] = False, keys: Literal[False] = False, default=None
) -> Iterable[tuple[_T, _T]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[True] = True, keys: Literal[False] = False, default=None
) -> Iterable[tuple[_T, _T, dict[str, Incomplete]]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: str = ..., keys: Literal[False] = False, default: _U = None
) -> Iterable[tuple[_T, _T, _U]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[False] = False, keys: Literal[True] = True, default=None
) -> Iterable[tuple[_T, _T, int]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: Literal[True] = True, keys: Literal[True] = True, default=None
) -> Iterable[tuple[_T, _T, int, dict[str, Incomplete]]]: ...
@overload
def selfloop_edges(
    G: Graph[_T], data: str = ..., keys: Literal[True] = ..., default: _U = None
) -> Iterable[tuple[_T, _T, int, _U]]: ...
def number_of_selfloops(G: Graph[Incomplete]) -> int: ...
