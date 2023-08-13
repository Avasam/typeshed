# Stubs for networkx.algorithms.similarity (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete
from operator import *

def graph_edit_distance(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
): ...
def optimal_edit_paths(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
): ...
def optimize_graph_edit_distance(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
) -> None: ...
def optimize_edit_paths(
    G1,
    G2,
    node_match: Incomplete | None = ...,
    edge_match: Incomplete | None = ...,
    node_subst_cost: Incomplete | None = ...,
    node_del_cost: Incomplete | None = ...,
    node_ins_cost: Incomplete | None = ...,
    edge_subst_cost: Incomplete | None = ...,
    edge_del_cost: Incomplete | None = ...,
    edge_ins_cost: Incomplete | None = ...,
    upper_bound: Incomplete | None = ...,
    strictly_decreasing: bool = ...,
): ...
