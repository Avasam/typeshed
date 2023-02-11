from collections.abc import Callable, Iterable
from typing import Any, TypeVar, overload
from typing_extensions import Final

_T = TypeVar("_T")
_S = TypeVar("_S")

__title__: Final[str]
__version__: Final[str]
__author__: Final[str]
__license__: Final[str]
__copyright__: Final[str]

@overload
def first(iterable: Iterable[_T]) -> _T | None: ...
@overload
def first(iterable: Iterable[_T], default: _S) -> _T | _S: ...
@overload
def first(iterable: Iterable[_T], default: _S, key: Callable[[_T], Any] | None) -> _T | _S: ...
@overload
def first(iterable: Iterable[_T], *, key: Callable[[_T], Any] | None) -> _T | None: ...
