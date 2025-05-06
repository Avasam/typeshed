from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

@_dispatchable
def spectral_graph_forge(
    G: Graph[Incomplete], alpha: float, transformation: str = "identity", seed: Incomplete | None = None
) -> Graph[Incomplete]: ...
