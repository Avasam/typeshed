"""@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.compiler.xla.service.hlo_pb2
import tensorflow.tsl.protobuf.error_codes_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CompilationResultProto(google.protobuf.message.Message):
    """Describes the result of a TPU compilation. This is also used as TPU
    compilation result status payload.
    URI: "type.googleapis.com/tensorflow.tpu.CompilationResultProto"
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ErrorCode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ErrorCodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[CompilationResultProto._ErrorCode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: CompilationResultProto._ErrorCode.ValueType  # 0
        OUT_OF_MEMORY: CompilationResultProto._ErrorCode.ValueType  # 1

    class ErrorCode(_ErrorCode, metaclass=_ErrorCodeEnumTypeWrapper): ...
    UNKNOWN: CompilationResultProto.ErrorCode.ValueType  # 0
    OUT_OF_MEMORY: CompilationResultProto.ErrorCode.ValueType  # 1

    STATUS_CODE_FIELD_NUMBER: builtins.int
    STATUS_ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    HLO_PROTOS_FIELD_NUMBER: builtins.int
    ERROR_CODE_FIELD_NUMBER: builtins.int
    status_code: tensorflow.tsl.protobuf.error_codes_pb2.Code.ValueType
    """The error message, if any, returned during compilation."""
    status_error_message: builtins.str
    error_code: global___CompilationResultProto.ErrorCode.ValueType
    @property
    def hlo_protos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.compiler.xla.service.hlo_pb2.HloProto]:
        """HLO proto."""

    def __init__(
        self,
        *,
        status_code: tensorflow.tsl.protobuf.error_codes_pb2.Code.ValueType | None = ...,
        status_error_message: builtins.str | None = ...,
        hlo_protos: collections.abc.Iterable[tensorflow.compiler.xla.service.hlo_pb2.HloProto] | None = ...,
        error_code: global___CompilationResultProto.ErrorCode.ValueType | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["error_code", b"error_code", "hlo_protos", b"hlo_protos", "status_code", b"status_code", "status_error_message", b"status_error_message"]) -> None: ...

global___CompilationResultProto = CompilationResultProto
