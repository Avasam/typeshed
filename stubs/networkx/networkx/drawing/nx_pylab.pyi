# Stubs for networkx.drawing.nx_pylab (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

def draw(G, pos: Incomplete | None = None, ax: Incomplete | None = None, **kwds) -> None: ...
def draw_networkx(G, pos: Incomplete | None = None, arrows: bool = ..., with_labels: bool = True, **kwds) -> None: ...
def draw_networkx_nodes(
    G,
    pos,
    nodelist: Incomplete | None = None,
    node_size: int = 300,
    node_color: str = "#1f78b4",
    node_shape: str = "o",
    alpha: float = ...,
    cmap: Incomplete | None = None,
    vmin: Incomplete | None = None,
    vmax: Incomplete | None = None,
    ax: Incomplete | None = None,
    linewidths: Incomplete | None = None,
    edgecolors: Incomplete | None = None,
    label: Incomplete | None = None,
    **kwds,
): ...
def draw_networkx_edges(
    G,
    pos,
    edgelist: Incomplete | None = None,
    width: float = 1.0,
    edge_color: str = "k",
    style: str = "solid",
    alpha: float = ...,
    arrowstyle: str = ...,
    arrowsize: int = 10,
    edge_cmap: Incomplete | None = None,
    edge_vmin: Incomplete | None = None,
    edge_vmax: Incomplete | None = None,
    ax: Incomplete | None = None,
    arrows: bool = ...,
    label: Incomplete | None = None,
    node_size: int = 300,
    nodelist: Incomplete | None = None,
    node_shape: str = "o",
    connectionstyle: Incomplete | None = "arc3",
    **kwds,
): ...
def draw_networkx_labels(
    G,
    pos,
    labels: Incomplete | None = None,
    font_size: int = 12,
    font_color: str = "k",
    font_family: str = "sans-serif",
    font_weight: str = "normal",
    alpha: float = ...,
    bbox: Incomplete | None = None,
    ax: Incomplete | None = None,
    **kwds,
): ...
def draw_networkx_edge_labels(
    G,
    pos,
    edge_labels: Incomplete | None = None,
    label_pos: float = 0.5,
    font_size: int = 10,
    font_color: str = "k",
    font_family: str = "sans-serif",
    font_weight: str = "normal",
    alpha: float = ...,
    bbox: Incomplete | None = None,
    ax: Incomplete | None = None,
    rotate: bool = True,
    **kwds,
): ...
def draw_circular(G, **kwargs) -> None: ...
def draw_kamada_kawai(G, **kwargs) -> None: ...
def draw_random(G, **kwargs) -> None: ...
def draw_spectral(G, **kwargs) -> None: ...
def draw_spring(G, **kwargs) -> None: ...
def draw_shell(G, **kwargs) -> None: ...
def draw_planar(G, **kwargs) -> None: ...
