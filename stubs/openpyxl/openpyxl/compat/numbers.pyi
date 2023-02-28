import sys
from decimal import Decimal
from typing import Any
from typing_extensions import TypeAlias

import numpy

if sys.version_info >= (3, 8):
    import numpy._typing

    _NBitBase: TypeAlias = numpy._typing.NBitBase
else:
    _NBitBase: TypeAlias = Any

_NumericTypes: TypeAlias = int | float | Decimal | numpy.bool_ | numpy.floating[_NBitBase] | numpy.integer[_NBitBase]
NUMERIC_TYPES: tuple[type[_NumericTypes], ...]

NUMPY: bool
