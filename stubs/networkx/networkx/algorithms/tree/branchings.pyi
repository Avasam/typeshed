from _typeshed import Incomplete

from .recognition import *

def branching_weight(G, attr: str = "weight", default: int = 1): ...
def greedy_branching(G, attr: str = "weight", default: int = 1, kind: str = "max", seed: Incomplete | None = None): ...

class Edmonds:
    G_original: Incomplete
    store: bool
    edges: Incomplete
    template: Incomplete
    def __init__(self, G, seed: Incomplete | None = None) -> None: ...
    def find_optimum(
        self,
        attr: str = "weight",
        default: int = 1,
        kind: str = "max",
        style: str = "branching",
        preserve_attrs: bool = False,
        seed: Incomplete | None = None,
    ): ...

def maximum_branching(G, attr: str = "weight", default: int = 1, preserve_attrs: bool = False): ...
def minimum_branching(G, attr: str = "weight", default: int = 1, preserve_attrs: bool = False): ...
def maximum_spanning_arborescence(G, attr: str = "weight", default: int = 1, preserve_attrs: bool = False): ...
def minimum_spanning_arborescence(G, attr: str = "weight", default: int = 1, preserve_attrs: bool = False): ...
