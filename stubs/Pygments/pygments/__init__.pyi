from _typeshed import SupportsWrite
from typing import TypeVar, overload
from typing_extensions import Final

from pygments.formatter import Formatter

_T = TypeVar("_T", str, bytes)

__version__: Final[str]
__docformat__: Final = "restructuredtext"
__all__ = ["lex", "format", "highlight"]

def lex(code, lexer): ...
@overload
def format(tokens, formatter: Formatter[_T], outfile: SupportsWrite[_T]) -> None: ...
@overload
def format(tokens, formatter: Formatter[_T], outfile: None = ...) -> _T: ...
@overload
def highlight(code, lexer, formatter: Formatter[_T], outfile: SupportsWrite[_T]) -> None: ...
@overload
def highlight(code, lexer, formatter: Formatter[_T], outfile: None = ...) -> _T: ...
