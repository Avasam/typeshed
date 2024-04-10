"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protobuf containing the metadata for each Keras object saved in a SavedModel."""
import builtins
import collections.abc
import typing as typing_extensions

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.python.keras.protobuf.versions_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SavedMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODES_FIELD_NUMBER: builtins.int
    @property
    def nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SavedObject]:
        """Nodes represent trackable objects in the SavedModel. The data for every
        Keras object is stored.
        """
    def __init__(
        self,
        *,
        nodes: collections.abc.Iterable[global___SavedObject] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nodes", b"nodes"]) -> None: ...

global___SavedMetadata = SavedMetadata

@typing_extensions.final
class SavedObject(google.protobuf.message.Message):
    """Metadata of an individual Keras object."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_ID_FIELD_NUMBER: builtins.int
    NODE_PATH_FIELD_NUMBER: builtins.int
    IDENTIFIER_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    node_id: builtins.int
    """Index of the node in the SavedModel SavedObjectGraph."""
    node_path: builtins.str
    """String path from root (e.g. "root.child_layer")"""
    identifier: builtins.str
    """Identifier to determine loading function.
    Must be one of:
      _tf_keras_input_layer, _tf_keras_layer, _tf_keras_metric,
      _tf_keras_model, _tf_keras_network, _tf_keras_rnn_layer,
      _tf_keras_sequential
    """
    metadata: builtins.str
    """Metadata containing a JSON-serialized object with the non-TensorFlow
    attributes for this Keras object.
    """
    @property
    def version(self) -> tensorflow.python.keras.protobuf.versions_pb2.VersionDef:
        """Version defined by the code serializing this Keras object."""
    def __init__(
        self,
        *,
        node_id: builtins.int | None = ...,
        node_path: builtins.str | None = ...,
        identifier: builtins.str | None = ...,
        metadata: builtins.str | None = ...,
        version: tensorflow.python.keras.protobuf.versions_pb2.VersionDef | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["identifier", b"identifier", "metadata", b"metadata", "node_id", b"node_id", "node_path", b"node_path", "version", b"version"]) -> None: ...

global___SavedObject = SavedObject
