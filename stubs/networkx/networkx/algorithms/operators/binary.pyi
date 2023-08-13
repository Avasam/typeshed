from _typeshed import Incomplete
from typing import TypeVar

from networkx.classes.digraph import DiGraph

def disjoint_union(G, H): ...
def intersection(G, H): ...
def difference(G, H): ...
def symmetric_difference(G, H): ...

_X = TypeVar("_X", covariant=True)
_Y = TypeVar("_Y", covariant=True)
# GT = TypeVar('GT', bound=Graph)
# TODO: This does not handle the cases when graphs of different types are passed which is allowed

def compose(G: DiGraph[_X], H: DiGraph[_Y]) -> DiGraph[_X | _Y]: ...
def union(G: DiGraph[_X], H: DiGraph[_Y], rename=(), name: Incomplete | None = ...) -> DiGraph[_X | _Y]: ...
