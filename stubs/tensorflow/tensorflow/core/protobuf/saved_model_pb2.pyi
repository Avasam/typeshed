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
import tensorflow.core.protobuf.meta_graph_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SavedModel(google.protobuf.message.Message):
    """
    SavedModel is the high level serialization format for TensorFlow Models.
    See [todo: doc links, similar to session_bundle] for more information.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SAVED_MODEL_SCHEMA_VERSION_FIELD_NUMBER: builtins.int
    META_GRAPHS_FIELD_NUMBER: builtins.int
    saved_model_schema_version: builtins.int
    """The schema version of the SavedModel instance. Used for versioning when
    making future changes to the specification/implementation. Initial value
    at release will be 1.
    """
    @property
    def meta_graphs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.protobuf.meta_graph_pb2.MetaGraphDef]:
        """One or more MetaGraphs."""

    def __init__(
        self,
        *,
        saved_model_schema_version: builtins.int | None = ...,
        meta_graphs: collections.abc.Iterable[tensorflow.core.protobuf.meta_graph_pb2.MetaGraphDef] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["meta_graphs", b"meta_graphs", "saved_model_schema_version", b"saved_model_schema_version"]) -> None: ...

global___SavedModel = SavedModel
