from _typeshed import Incomplete
from collections.abc import Iterable
from typing import TypeVar, overload
from typing_extensions import Literal

from networkx.classes.graph import Graph

_T = TypeVar("_T")
_U = TypeVar("_U")

@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[False] = False,
    keys: Literal[False] = False,
    default=...,
) -> Iterable[tuple[_T, _T]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[True] = True,
    keys: Literal[False] = False,
    default=...,
) -> Iterable[tuple[_T, _T, dict[str, Incomplete]]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: str = ...,
    keys: Literal[False] = False,
    default: _U = None,
) -> Iterable[tuple[_T, _T, dict[str, _U]]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[False] = False,
    keys: Literal[True] = True,
    default=...,
) -> Iterable[tuple[_T, _T, int]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: Literal[True] = True,
    keys: Literal[True] = True,
    default=...,
) -> Iterable[tuple[_T, _T, int, dict[str, Incomplete]]]: ...
@overload
def edge_boundary(
    G: Graph[_T],
    nbunch1: Iterable[_T],
    nbunch2: Iterable[_T] | None = ...,
    data: str = ...,
    keys: Literal[True] = True,
    default: _U = None,
) -> Iterable[tuple[_T, _T, int, dict[str, _U]]]: ...
def node_boundary(G: Graph[_T], nbunch1: Iterable[_T], nbunch2: Iterable[_T] | None = ...) -> Iterable[_T]: ...
