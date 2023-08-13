from _typeshed import Incomplete

def quotient_graph(
    G,
    partition,
    edge_relation: Incomplete | None = None,
    node_data: Incomplete | None = None,
    edge_data: Incomplete | None = None,
    relabel: bool = False,
    create_using: Incomplete | None = None,
): ...
def contracted_nodes(G, u, v, self_loops: bool = True): ...

identified_nodes = contracted_nodes

def contracted_edge(G, edge, self_loops: bool = True): ...
