"""@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Race:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _RaceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Race.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NoRace: _Race.ValueType  # 0
    Terran: _Race.ValueType  # 1
    Zerg: _Race.ValueType  # 2
    Protoss: _Race.ValueType  # 3
    Random: _Race.ValueType  # 4

class Race(_Race, metaclass=_RaceEnumTypeWrapper): ...

NoRace: Race.ValueType  # 0
Terran: Race.ValueType  # 1
Zerg: Race.ValueType  # 2
Protoss: Race.ValueType  # 3
Random: Race.ValueType  # 4
global___Race = Race

@typing.final
class AvailableAbility(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ABILITY_ID_FIELD_NUMBER: builtins.int
    REQUIRES_POINT_FIELD_NUMBER: builtins.int
    ability_id: builtins.int
    requires_point: builtins.bool
    def __init__(
        self,
        *,
        ability_id: builtins.int | None = ...,
        requires_point: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ability_id", b"ability_id", "requires_point", b"requires_point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["ability_id", b"ability_id", "requires_point", b"requires_point"]) -> None: ...

global___AvailableAbility = AvailableAbility

@typing.final
class ImageData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BITS_PER_PIXEL_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    bits_per_pixel: builtins.int
    """Number of bits per pixel; 8 bits for a byte etc."""
    data: builtins.bytes
    """Binary data; the size of this buffer in bytes is width * height * bits_per_pixel / 8."""
    @property
    def size(self) -> global___Size2DI:
        """Dimension in pixels."""

    def __init__(
        self,
        *,
        bits_per_pixel: builtins.int | None = ...,
        size: global___Size2DI | None = ...,
        data: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bits_per_pixel", b"bits_per_pixel", "data", b"data", "size", b"size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bits_per_pixel", b"bits_per_pixel", "data", b"data", "size", b"size"]) -> None: ...

global___ImageData = ImageData

@typing.final
class PointI(google.protobuf.message.Message):
    """Point on the screen/minimap (e.g., 0..64).
    Note: bottom left of the screen is 0, 0.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    x: builtins.int
    y: builtins.int
    def __init__(
        self,
        *,
        x: builtins.int | None = ...,
        y: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> None: ...

global___PointI = PointI

@typing.final
class RectangleI(google.protobuf.message.Message):
    """Screen space rectangular area."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    P0_FIELD_NUMBER: builtins.int
    P1_FIELD_NUMBER: builtins.int
    @property
    def p0(self) -> global___PointI: ...
    @property
    def p1(self) -> global___PointI: ...
    def __init__(
        self,
        *,
        p0: global___PointI | None = ...,
        p1: global___PointI | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["p0", b"p0", "p1", b"p1"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["p0", b"p0", "p1", b"p1"]) -> None: ...

global___RectangleI = RectangleI

@typing.final
class Point2D(google.protobuf.message.Message):
    """Point on the game board, 0..255.
    Note: bottom left of the screen is 0, 0.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float | None = ...,
        y: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> None: ...

global___Point2D = Point2D

@typing.final
class Point(google.protobuf.message.Message):
    """Point on the game board, 0..255.
    Note: bottom left of the screen is 0, 0.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float | None = ...,
        y: builtins.float | None = ...,
        z: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["x", b"x", "y", b"y", "z", b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Point = Point

@typing.final
class Size2DI(google.protobuf.message.Message):
    """Screen dimensions."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    x: builtins.int
    y: builtins.int
    def __init__(
        self,
        *,
        x: builtins.int | None = ...,
        y: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["x", b"x", "y", b"y"]) -> None: ...

global___Size2DI = Size2DI
