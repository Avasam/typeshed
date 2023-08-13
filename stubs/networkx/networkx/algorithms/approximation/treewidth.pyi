# Stubs for networkx.algorithms.approximation.treewidth (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

def treewidth_min_degree(G): ...
def treewidth_min_fill_in(G): ...

class MinDegreeHeuristic:
    def __init__(self, graph) -> None: ...
    def best_node(self, graph): ...
