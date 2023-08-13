from _typeshed import Incomplete

def random_layout(G, center: Incomplete | None = None, dim: int = 2, seed: Incomplete | None = None): ...
def circular_layout(G, scale: int = 1, center: Incomplete | None = None, dim: int = 2): ...
def shell_layout(G, nlist: Incomplete | None = None, scale: int = 1, center: Incomplete | None = None, dim: int = 2): ...
def bipartite_layout(G, nodes, align: str = "vertical", scale: int = 1, center: Incomplete | None = None, aspect_ratio=...): ...
def fruchterman_reingold_layout(
    G,
    k: Incomplete | None = None,
    pos: Incomplete | None = None,
    fixed: Incomplete | None = None,
    iterations: int = 50,
    threshold: float = 0.0001,
    weight: str = "weight",
    scale: int = 1,
    center: Incomplete | None = None,
    dim: int = 2,
    seed: Incomplete | None = None,
): ...

spring_layout = fruchterman_reingold_layout

def kamada_kawai_layout(
    G,
    dist: Incomplete | None = None,
    pos: Incomplete | None = None,
    weight: str = "weight",
    scale: int = 1,
    center: Incomplete | None = None,
    dim: int = 2,
): ...
def spectral_layout(G, weight: str = "weight", scale: int = 1, center: Incomplete | None = None, dim: int = 2): ...
def planar_layout(G, scale: int = 1, center: Incomplete | None = None, dim: int = 2): ...
def rescale_layout(pos, scale: int = 1): ...
