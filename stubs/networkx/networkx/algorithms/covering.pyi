from _typeshed import Incomplete
from collections.abc import Callable, Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["min_edge_cover", "is_edge_cover"]

@_dispatchable
def min_edge_cover(G: Graph[_Node], matching_algorithm: Callable[..., Incomplete] | None = None) -> set[Incomplete]: ...
@_dispatchable
def is_edge_cover(G: Graph[_Node], cover: Iterable[Iterable[Incomplete]]) -> bool: ...
