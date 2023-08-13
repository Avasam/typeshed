# Stubs for networkx.utils.misc (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _typeshed import Incomplete

basestring = str
unicode = str

def is_string_like(obj): ...
def iterable(obj): ...
def flatten(obj, result: Incomplete | None = ...): ...
def is_list_of_ints(intlist): ...

PY2: Incomplete

def make_str(x): ...
def generate_unique_node(): ...
def default_opener(filename) -> None: ...
def dict_to_numpy_array(d, mapping: Incomplete | None = ...): ...
def dict_to_numpy_array2(d, mapping: Incomplete | None = ...): ...
def dict_to_numpy_array1(d, mapping: Incomplete | None = ...): ...
def is_iterator(obj): ...
def arbitrary_element(iterable): ...
def consume(iterator) -> None: ...
def pairwise(iterable, cyclic: bool = ...): ...
def groups(many_to_one): ...
def to_tuple(x): ...
def create_random_state(random_state: Incomplete | None = ...): ...

class PythonRandomInterface:
    def __init__(self, rng: Incomplete | None = ...) -> None: ...
    msg: str = ...
    def random(self): ...
    def uniform(self, a, b): ...
    def randrange(self, a, b: Incomplete | None = ...): ...
    def choice(self, seq): ...
    def gauss(self, mu, sigma): ...
    def shuffle(self, seq): ...
    def sample(self, seq, k): ...
    def randint(self, a, b): ...
    def expovariate(self, scale): ...
    def paretovariate(self, shape): ...

def create_py_random_state(random_state: Incomplete | None = ...): ...
def setup_module(module) -> None: ...
