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
import tensorflow.core.framework.tensor_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SnapshotRecord(google.protobuf.message.Message):
    """
    Each SnapshotRecord represents one batch of pre-processed input data. A batch
    consists of a list of tensors that we encode as TensorProtos. This message
    doesn't store the structure of the batch.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_FIELD_NUMBER: builtins.int
    @property
    def tensor(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.tensor_pb2.TensorProto]: ...
    def __init__(
        self,
        *,
        tensor: collections.abc.Iterable[tensorflow.core.framework.tensor_pb2.TensorProto] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tensor", b"tensor"]) -> None: ...

global___SnapshotRecord = SnapshotRecord

@typing.final
class SnapshotMetadataRecord(google.protobuf.message.Message):
    """This stores the metadata information present in each snapshot record."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRAPH_HASH_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    CREATION_TIMESTAMP_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    NUM_ELEMENTS_FIELD_NUMBER: builtins.int
    FINALIZED_FIELD_NUMBER: builtins.int
    graph_hash: builtins.str
    """Stores the fingerprint of the graph that describes the dataset that is
    snapshotted.
    """
    run_id: builtins.str
    """Run ID that this snapshot corresponds to."""
    creation_timestamp: builtins.int
    """Time when we started creating this snapshot."""
    version: builtins.int
    """Version of the snapshot data file format."""
    num_elements: builtins.int
    """The number of elements in the snapshot."""
    finalized: builtins.bool
    @property
    def dtype(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[tensorflow.core.framework.types_pb2.DataType.ValueType]:
        """A list of tensor dtype corresponding to each element of the snapshot."""

    def __init__(
        self,
        *,
        graph_hash: builtins.str | None = ...,
        run_id: builtins.str | None = ...,
        creation_timestamp: builtins.int | None = ...,
        version: builtins.int | None = ...,
        dtype: collections.abc.Iterable[tensorflow.core.framework.types_pb2.DataType.ValueType] | None = ...,
        num_elements: builtins.int | None = ...,
        finalized: builtins.bool | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["creation_timestamp", b"creation_timestamp", "dtype", b"dtype", "finalized", b"finalized", "graph_hash", b"graph_hash", "num_elements", b"num_elements", "run_id", b"run_id", "version", b"version"]) -> None: ...

global___SnapshotMetadataRecord = SnapshotMetadataRecord

@typing.final
class TensorMetadata(google.protobuf.message.Message):
    """Metadata for a single tensor in the Snapshot Record."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_SHAPE_FIELD_NUMBER: builtins.int
    TENSOR_SIZE_BYTES_FIELD_NUMBER: builtins.int
    tensor_size_bytes: builtins.int
    """Number of uncompressed bytes used to store the tensor representation."""
    @property
    def tensor_shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    def __init__(
        self,
        *,
        tensor_shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        tensor_size_bytes: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tensor_shape", b"tensor_shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["tensor_shape", b"tensor_shape", "tensor_size_bytes", b"tensor_size_bytes"]) -> None: ...

global___TensorMetadata = TensorMetadata

@typing.final
class SnapshotTensorMetadata(google.protobuf.message.Message):
    """Metadata for all the tensors in a Snapshot Record."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TENSOR_METADATA_FIELD_NUMBER: builtins.int
    @property
    def tensor_metadata(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TensorMetadata]: ...
    def __init__(
        self,
        *,
        tensor_metadata: collections.abc.Iterable[global___TensorMetadata] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["tensor_metadata", b"tensor_metadata"]) -> None: ...

global___SnapshotTensorMetadata = SnapshotTensorMetadata

@typing.final
class DistributedSnapshotMetadata(google.protobuf.message.Message):
    """Metadata for a `tf.data.Dataset` distributed snapshot."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ELEMENT_SPEC_FIELD_NUMBER: builtins.int
    COMPRESSION_FIELD_NUMBER: builtins.int
    element_spec: builtins.bytes
    """The element spec of the snapshotted dataset."""
    compression: builtins.str
    """Whether and how to compress the snapshot.  Supported values are defined in
    `tsl::io::compression`.  In particular, an empty string specifies not to
    compress.
    """
    def __init__(
        self,
        *,
        element_spec: builtins.bytes | None = ...,
        compression: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["compression", b"compression", "element_spec", b"element_spec"]) -> None: ...

global___DistributedSnapshotMetadata = DistributedSnapshotMetadata
