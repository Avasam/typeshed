# Stubs for networkx.algorithms.dag (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete
from typing import TypeVar

from networkx.classes.graph import Graph

_T = TypeVar("_T")

def descendants(G: Graph[_T], source: _T) -> set[_T]: ...
def ancestors(G: Graph[_T], source: _T) -> set[_T]: ...
def is_directed_acyclic_graph(G): ...
def topological_sort(G) -> None: ...
def lexicographical_topological_sort(G, key: Incomplete | None = ...): ...
def all_topological_sorts(G) -> None: ...
def is_aperiodic(G): ...
def transitive_closure(G): ...
def transitive_reduction(G): ...
def antichains(G) -> None: ...
def dag_longest_path(G, weight: str = ..., default_weight: int = ...): ...
def dag_longest_path_length(G, weight: str = ..., default_weight: int = ...): ...
def dag_to_branching(G): ...
