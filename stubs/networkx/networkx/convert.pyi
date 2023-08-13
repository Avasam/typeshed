from _typeshed import Incomplete
from collections.abc import Iterable
from typing_extensions import TypeAlias

import numpy
from networkx.classes.graph import EdgePlus, Graph, _Node

Data: TypeAlias = (
    Graph[_Node]
    | dict[_Node, dict[_Node, dict[str, Incomplete]]]
    | dict[_Node, Iterable[_Node]]
    | Iterable[EdgePlus[_Node]]
    | numpy.ndarray[_Node, Incomplete]
    # scipy is untyped
    # | scipy.sparse.base.spmatrix
)
