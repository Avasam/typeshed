import enum
from collections.abc import Sequence
from ctypes import _CVoidConstPLike
from typing import Any
from typing_extensions import Literal, TypeAlias

import numpy
import numpy.typing
from PIL import Image
from torch import Tensor

_Frame: TypeAlias = Image.Image | numpy.typing.NDArray[numpy.int32] | numpy.typing.NDArray[numpy.float32] | Tensor

class CaptureOutputs(enum.Enum):
    PIL: int
    NUMPY: int
    NUMPY_FLOAT: int
    PYTORCH: int
    PYTORCH_FLOAT: int
    PYTORCH_GPU: int
    PYTORCH_FLOAT_GPU: int

class CaptureOutputError(BaseException): ...

# All CaptureOutput methods just reference the backend. Making this both a base class and a wrapper.
class CaptureOutput:
    # `backend` is a subclass of CaptureOutput based on the CaptureOutputs enum passed to __init__
    backend: CaptureOutput
    def __init__(self, backend: CaptureOutputs = ...) -> None: ...
    def process(
        self,
        pointer: _CVoidConstPLike,
        pitch: int,
        size: int,
        width: int,
        height: int,
        region: tuple[int, int, int, int],
        rotation: int,
    ) -> Any: ...  # AnyOf[_Frame]
    def to_pil(self, frame: _Frame) -> Image.Image: ...
    def stack(self, frames: Sequence[_Frame], stack_dimension: Literal["first", "last"]) -> Any: ...  # AnyOf[_Frame]
