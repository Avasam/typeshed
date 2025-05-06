from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

@_dispatchable
def partial_duplication_graph(N: int, n: int, p: float, q: float, seed: Incomplete | None = None): ...
@_dispatchable
def duplication_divergence_graph(n: int, p: float, seed: Incomplete | None = None) -> Graph[Incomplete]: ...
