import numbers
import sys
from _typeshed import Self
from collections.abc import Container, Sequence
from types import TracebackType
from typing import Any, ClassVar, NamedTuple, Union, overload
from typing_extensions import Literal, TypeAlias

_Decimal: TypeAlias = Decimal | int
_DecimalNew: TypeAlias = Union[Decimal, float, str, tuple[int, Sequence[int], int]]
_ComparableNum: TypeAlias = Decimal | float | numbers.Rational

__version__: str
__libmpdec_version__: str

class DecimalTuple(NamedTuple):
    sign: int
    digits: tuple[int, ...]
    exponent: int | Literal["n", "N", "F"]

ROUND_DOWN: str
ROUND_HALF_UP: str
ROUND_HALF_EVEN: str
ROUND_CEILING: str
ROUND_FLOOR: str
ROUND_UP: str
ROUND_HALF_DOWN: str
ROUND_05UP: str
HAVE_CONTEXTVAR: bool
HAVE_THREADS: bool
MAX_EMAX: int
MAX_PREC: int
MIN_EMIN: int
MIN_ETINY: int

class DecimalException(ArithmeticError): ...
class Clamped(DecimalException): ...
class InvalidOperation(DecimalException): ...
class ConversionSyntax(InvalidOperation): ...
class DivisionByZero(DecimalException, ZeroDivisionError): ...
class DivisionImpossible(InvalidOperation): ...
class DivisionUndefined(InvalidOperation, ZeroDivisionError): ...
class Inexact(DecimalException): ...
class InvalidContext(InvalidOperation): ...
class Rounded(DecimalException): ...
class Subnormal(DecimalException): ...
class Overflow(Inexact, Rounded): ...
class Underflow(Inexact, Rounded, Subnormal): ...
class FloatOperation(DecimalException, TypeError): ...

def setcontext(__context: Context) -> None: ...
def getcontext() -> Context: ...

if sys.version_info >= (3, 11):
    def localcontext(
        ctx: Context | None = None,
        *,
        prec: int | None = ...,
        rounding: str | None = ...,
        Emin: int | None = ...,
        Emax: int | None = ...,
        capitals: int | None = ...,
        clamp: int | None = ...,
        traps: dict[_TrapType, bool] | None = ...,
        flags: dict[_TrapType, bool] | None = ...,
    ) -> _ContextManager: ...

else:
    def localcontext(ctx: Context | None = None) -> _ContextManager: ...

class Decimal:
    def __new__(cls: type[Self], value: _DecimalNew = ..., context: Context | None = ...) -> Self: ...
    @classmethod
    def from_float(cls: type[Self], __f: float) -> Self: ...
    def __bool__(self) -> bool: ...
    def compare(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def as_tuple(self) -> DecimalTuple: ...
    def as_integer_ratio(self) -> tuple[int, int]: ...
    def to_eng_string(self, context: Context | None = None) -> str: ...
    def __abs__(self) -> Decimal: ...
    def __add__(self, __other: _Decimal) -> Decimal: ...
    def __divmod__(self, __other: _Decimal) -> tuple[Decimal, Decimal]: ...
    def __eq__(self, __other: object) -> bool: ...
    def __floordiv__(self, __other: _Decimal) -> Decimal: ...
    def __ge__(self, __other: _ComparableNum) -> bool: ...
    def __gt__(self, __other: _ComparableNum) -> bool: ...
    def __le__(self, __other: _ComparableNum) -> bool: ...
    def __lt__(self, __other: _ComparableNum) -> bool: ...
    def __mod__(self, __other: _Decimal) -> Decimal: ...
    def __mul__(self, __other: _Decimal) -> Decimal: ...
    def __neg__(self) -> Decimal: ...
    def __pos__(self) -> Decimal: ...
    def __pow__(self, __other: _Decimal, __modulo: _Decimal | None = ...) -> Decimal: ...
    def __radd__(self, __other: _Decimal) -> Decimal: ...
    def __rdivmod__(self, __other: _Decimal) -> tuple[Decimal, Decimal]: ...
    def __rfloordiv__(self, __other: _Decimal) -> Decimal: ...
    def __rmod__(self, __other: _Decimal) -> Decimal: ...
    def __rmul__(self, __other: _Decimal) -> Decimal: ...
    def __rsub__(self, __other: _Decimal) -> Decimal: ...
    def __rtruediv__(self, __other: _Decimal) -> Decimal: ...
    def __sub__(self, __other: _Decimal) -> Decimal: ...
    def __truediv__(self, __other: _Decimal) -> Decimal: ...
    def remainder_near(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __trunc__(self) -> int: ...
    @property
    def real(self) -> Decimal: ...
    @property
    def imag(self) -> Decimal: ...
    def conjugate(self) -> Decimal: ...
    def __complex__(self) -> complex: ...
    @overload
    def __round__(self) -> int: ...
    @overload
    def __round__(self, __ndigits: int) -> Decimal: ...
    def __floor__(self) -> int: ...
    def __ceil__(self) -> int: ...
    def fma(self, other: _Decimal, third: _Decimal, context: Context | None = None) -> Decimal: ...
    def __rpow__(self, __other: _Decimal, __context: Context | None = ...) -> Decimal: ...
    def normalize(self, context: Context | None = None) -> Decimal: ...
    def quantize(self, exp: _Decimal, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def same_quantum(self, other: _Decimal, context: Context | None = None) -> bool: ...
    def to_integral_exact(self, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def to_integral_value(self, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def to_integral(self, rounding: str | None = None, context: Context | None = None) -> Decimal: ...
    def sqrt(self, context: Context | None = None) -> Decimal: ...
    def max(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def min(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def adjusted(self) -> int: ...
    def canonical(self) -> Decimal: ...
    def compare_signal(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def compare_total(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def compare_total_mag(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def copy_abs(self) -> Decimal: ...
    def copy_negate(self) -> Decimal: ...
    def copy_sign(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def exp(self, context: Context | None = None) -> Decimal: ...
    def is_canonical(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_infinite(self) -> bool: ...
    def is_nan(self) -> bool: ...
    def is_normal(self, context: Context | None = None) -> bool: ...
    def is_qnan(self) -> bool: ...
    def is_signed(self) -> bool: ...
    def is_snan(self) -> bool: ...
    def is_subnormal(self, context: Context | None = None) -> bool: ...
    def is_zero(self) -> bool: ...
    def ln(self, context: Context | None = None) -> Decimal: ...
    def log10(self, context: Context | None = None) -> Decimal: ...
    def logb(self, context: Context | None = None) -> Decimal: ...
    def logical_and(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def logical_invert(self, context: Context | None = None) -> Decimal: ...
    def logical_or(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def logical_xor(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def max_mag(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def min_mag(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def next_minus(self, context: Context | None = None) -> Decimal: ...
    def next_plus(self, context: Context | None = None) -> Decimal: ...
    def next_toward(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def number_class(self, context: Context | None = None) -> str: ...
    def radix(self) -> Decimal: ...
    def rotate(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def scaleb(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def shift(self, other: _Decimal, context: Context | None = None) -> Decimal: ...
    def __reduce__(self: Self) -> tuple[type[Self], tuple[str]]: ...
    def __copy__(self: Self) -> Self: ...
    def __deepcopy__(self: Self, __memo: Any) -> Self: ...
    def __format__(self, __specifier: str, __context: Context | None = ...) -> str: ...

class _ContextManager:
    new_context: Context
    saved_context: Context
    def __init__(self, new_context: Context) -> None: ...
    def __enter__(self) -> Context: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...

_TrapType: TypeAlias = type[DecimalException]

class Context:
    # TODO: Context doesn't allow you to delete *any* attributes from instances of the class at runtime,
    # even settable attributes like `prec` and `rounding`,
    # but that's inexpressable in the stub.
    # Type checkers either ignore it or misinterpret it
    # if you add a `def __delattr__(self, __name: str) -> NoReturn` method to the stub
    prec: int
    rounding: str
    Emin: int
    Emax: int
    capitals: int
    clamp: int
    traps: dict[_TrapType, bool]
    flags: dict[_TrapType, bool]
    def __init__(
        self,
        prec: int | None = ...,
        rounding: str | None = ...,
        Emin: int | None = ...,
        Emax: int | None = ...,
        capitals: int | None = ...,
        clamp: int | None = ...,
        flags: None | dict[_TrapType, bool] | Container[_TrapType] = ...,
        traps: None | dict[_TrapType, bool] | Container[_TrapType] = ...,
        _ignored_flags: list[_TrapType] | None = ...,
    ) -> None: ...
    def __reduce__(self: Self) -> tuple[type[Self], tuple[Any, ...]]: ...
    def clear_flags(self) -> None: ...
    def clear_traps(self) -> None: ...
    def copy(self) -> Context: ...
    def __copy__(self) -> Context: ...
    # see https://github.com/python/cpython/issues/94107
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def Etiny(self) -> int: ...
    def Etop(self) -> int: ...
    def create_decimal(self, __num: _DecimalNew = ...) -> Decimal: ...
    def create_decimal_from_float(self, __f: float) -> Decimal: ...
    def abs(self, __x: _Decimal) -> Decimal: ...
    def add(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def canonical(self, __x: Decimal) -> Decimal: ...
    def compare(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def compare_signal(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def compare_total(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def compare_total_mag(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def copy_abs(self, __x: _Decimal) -> Decimal: ...
    def copy_decimal(self, __x: _Decimal) -> Decimal: ...
    def copy_negate(self, __x: _Decimal) -> Decimal: ...
    def copy_sign(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def divide(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def divide_int(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def divmod(self, __x: _Decimal, __y: _Decimal) -> tuple[Decimal, Decimal]: ...
    def exp(self, __x: _Decimal) -> Decimal: ...
    def fma(self, __x: _Decimal, __y: _Decimal, __z: _Decimal) -> Decimal: ...
    def is_canonical(self, __x: _Decimal) -> bool: ...
    def is_finite(self, __x: _Decimal) -> bool: ...
    def is_infinite(self, __x: _Decimal) -> bool: ...
    def is_nan(self, __x: _Decimal) -> bool: ...
    def is_normal(self, __x: _Decimal) -> bool: ...
    def is_qnan(self, __x: _Decimal) -> bool: ...
    def is_signed(self, __x: _Decimal) -> bool: ...
    def is_snan(self, __x: _Decimal) -> bool: ...
    def is_subnormal(self, __x: _Decimal) -> bool: ...
    def is_zero(self, __x: _Decimal) -> bool: ...
    def ln(self, __x: _Decimal) -> Decimal: ...
    def log10(self, __x: _Decimal) -> Decimal: ...
    def logb(self, __x: _Decimal) -> Decimal: ...
    def logical_and(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def logical_invert(self, __x: _Decimal) -> Decimal: ...
    def logical_or(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def logical_xor(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def max(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def max_mag(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def min(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def min_mag(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def minus(self, __x: _Decimal) -> Decimal: ...
    def multiply(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def next_minus(self, __x: _Decimal) -> Decimal: ...
    def next_plus(self, __x: _Decimal) -> Decimal: ...
    def next_toward(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def normalize(self, __x: _Decimal) -> Decimal: ...
    def number_class(self, __x: _Decimal) -> str: ...
    def plus(self, __x: _Decimal) -> Decimal: ...
    def power(self, a: _Decimal, b: _Decimal, modulo: _Decimal | None = None) -> Decimal: ...
    def quantize(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def radix(self) -> Decimal: ...
    def remainder(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def remainder_near(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def rotate(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def same_quantum(self, __x: _Decimal, __y: _Decimal) -> bool: ...
    def scaleb(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def shift(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def sqrt(self, __x: _Decimal) -> Decimal: ...
    def subtract(self, __x: _Decimal, __y: _Decimal) -> Decimal: ...
    def to_eng_string(self, __x: _Decimal) -> str: ...
    def to_sci_string(self, __x: _Decimal) -> str: ...
    def to_integral_exact(self, __x: _Decimal) -> Decimal: ...
    def to_integral_value(self, __x: _Decimal) -> Decimal: ...
    def to_integral(self, __x: _Decimal) -> Decimal: ...

DefaultContext: Context
BasicContext: Context
ExtendedContext: Context
