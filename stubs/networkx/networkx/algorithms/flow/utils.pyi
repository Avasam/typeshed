# Stubs for networkx.algorithms.flow.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

class CurrentEdge:
    def __init__(self, edges) -> None: ...
    def get(self): ...
    def move_to_next(self) -> None: ...

class Level:
    active: Incomplete
    inactive: Incomplete
    def __init__(self) -> None: ...

class GlobalRelabelThreshold:
    def __init__(self, n, m, freq) -> None: ...
    def add_work(self, work) -> None: ...
    def is_reached(self): ...
    def clear_work(self) -> None: ...

def build_residual_network(G, capacity): ...
def detect_unboundedness(R, s, t) -> None: ...
def build_flow_dict(G, R): ...
