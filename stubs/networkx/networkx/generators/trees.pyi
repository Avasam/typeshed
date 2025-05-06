from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph

@_dispatchable
def prefix_tree(paths) -> DiGraph: ...
@_dispatchable
def prefix_tree_recursive(paths) -> DiGraph: ...
