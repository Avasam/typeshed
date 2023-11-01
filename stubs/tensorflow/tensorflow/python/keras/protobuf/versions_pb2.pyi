"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import sys

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class VersionDef(google.protobuf.message.Message):
    """This file is a copy of the TensorFlow Versions proto.
    Keep this file in sync with the source proto definition at
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/versions.proto

    Version information for a piece of serialized data

    There are different types of versions for each type of data
    (GraphDef, etc.), but they all have the same common shape
    described here.

    Each consumer has "consumer" and "min_producer" versions (specified
    elsewhere).  A consumer is allowed to consume this data if

      producer >= min_producer
      consumer >= min_consumer
      consumer not in bad_consumers

    LINT.IfChange
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRODUCER_FIELD_NUMBER: builtins.int
    MIN_CONSUMER_FIELD_NUMBER: builtins.int
    BAD_CONSUMERS_FIELD_NUMBER: builtins.int
    producer: builtins.int
    """The version of the code that produced this data."""
    min_consumer: builtins.int
    """Any consumer below this version is not allowed to consume this data."""
    @property
    def bad_consumers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Specific consumer versions which are disallowed (e.g. due to bugs)."""
    def __init__(
        self,
        *,
        producer: builtins.int | None = ...,
        min_consumer: builtins.int | None = ...,
        bad_consumers: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bad_consumers", b"bad_consumers", "min_consumer", b"min_consumer", "producer", b"producer"]) -> None: ...

global___VersionDef = VersionDef
