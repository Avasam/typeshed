from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Generic, TypeVar

import networkx as nx

def check_planarity(G, counterexample: bool = False): ...

_N = TypeVar("_N")

class Interval:
    low: Incomplete = ...
    high: Incomplete = ...
    def __init__(self, low: Incomplete | None = None, high: Incomplete | None = None) -> None: ...
    def empty(self): ...
    def copy(self): ...
    def conflicting(self, b, planarity_state): ...

class ConflictPair:
    left: Incomplete = ...
    right: Incomplete = ...
    def __init__(self, left=..., right=...) -> None: ...
    def swap(self) -> None: ...
    def lowest(self, planarity_state): ...

class LRPlanarity:
    G: Incomplete = ...
    roots: Incomplete = ...
    height: Incomplete = ...
    lowpt: Incomplete = ...
    lowpt2: Incomplete = ...
    nesting_depth: Incomplete = ...
    parent_edge: Incomplete = ...
    DG: Incomplete = ...
    adjs: Incomplete = ...
    ordered_adjs: Incomplete = ...
    ref: Incomplete = ...
    side: Incomplete = ...
    S: Incomplete = ...
    stack_bottom: Incomplete = ...
    lowpt_edge: Incomplete = ...
    left_ref: Incomplete = ...
    right_ref: Incomplete = ...
    embedding: Incomplete = ...
    def __init__(self, G) -> None: ...
    def lr_planarity(self): ...
    def lr_planarity_recursive(self): ...
    def dfs_orientation(self, v): ...
    def dfs_orientation_recursive(self, v) -> None: ...
    def dfs_testing(self, v): ...
    def dfs_testing_recursive(self, v): ...
    def add_constraints(self, ei, e): ...
    def remove_back_edges(self, e) -> None: ...
    def dfs_embedding(self, v): ...
    def dfs_embedding_recursive(self, v) -> None: ...
    def sign(self, e): ...
    def sign_recursive(self, e): ...

class PlanarEmbedding(Generic[_N], nx.DiGraph[_N]):
    def get_data(self) -> dict[_N, list[_N]]: ...
    def set_data(self, data: dict[_N, list[_N]]) -> None: ...
    def neighbors_cw_order(self, v: _N) -> Iterable[_N]: ...
    def check_structure(self) -> None: ...
    def add_half_edge_ccw(self, start_node: _N, end_node: _N, reference_neighbor: _N) -> None: ...
    def add_half_edge_cw(self, start_node: _N, end_node: _N, reference_neighbor: _N) -> None: ...
    def connect_components(self, v: _N, w: _N) -> None: ...
    def add_half_edge_first(self, start_node: _N, end_node: _N) -> None: ...
    def next_face_half_edge(self, v: _N, w: _N) -> tuple[_N, _N]: ...
    def traverse_face(self, v: _N, w: _N, mark_half_edges: set[tuple[_N, _N]] | None = None) -> list[_N]: ...
    def is_directed(self) -> bool: ...
