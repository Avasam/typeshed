"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.tsl.protobuf.error_codes_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class QueueRunnerDef(google.protobuf.message.Message):
    """Protocol buffer representing a QueueRunner."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    QUEUE_NAME_FIELD_NUMBER: builtins.int
    ENQUEUE_OP_NAME_FIELD_NUMBER: builtins.int
    CLOSE_OP_NAME_FIELD_NUMBER: builtins.int
    CANCEL_OP_NAME_FIELD_NUMBER: builtins.int
    QUEUE_CLOSED_EXCEPTION_TYPES_FIELD_NUMBER: builtins.int
    queue_name: builtins.str
    """Queue name."""
    close_op_name: builtins.str
    """The operation to run to close the queue."""
    cancel_op_name: builtins.str
    """The operation to run to cancel the queue."""
    @property
    def enqueue_op_name(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """A list of enqueue operations."""

    @property
    def queue_closed_exception_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[tensorflow.tsl.protobuf.error_codes_pb2.Code.ValueType]:
        """
        A list of exception types considered to signal a safely closed queue
        if raised during enqueue operations.
        """

    def __init__(
        self,
        *,
        queue_name: builtins.str | None = ...,
        enqueue_op_name: collections.abc.Iterable[builtins.str] | None = ...,
        close_op_name: builtins.str | None = ...,
        cancel_op_name: builtins.str | None = ...,
        queue_closed_exception_types: collections.abc.Iterable[tensorflow.tsl.protobuf.error_codes_pb2.Code.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cancel_op_name", b"cancel_op_name", "close_op_name", b"close_op_name", "enqueue_op_name", b"enqueue_op_name", "queue_closed_exception_types", b"queue_closed_exception_types", "queue_name", b"queue_name"]) -> None: ...

global___QueueRunnerDef = QueueRunnerDef
