"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import tensorflow.core.framework.versions_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FingerprintDef(google.protobuf.message.Message):
    """Protocol buffer representing a SavedModel Fingerprint.

    If there are multiple MetaGraphDefs in the SavedModel, the FingerprintDef
    corresponds to the first one.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRAPH_DEF_CHECKSUM_FIELD_NUMBER: builtins.int
    GRAPH_DEF_PROGRAM_HASH_FIELD_NUMBER: builtins.int
    SIGNATURE_DEF_HASH_FIELD_NUMBER: builtins.int
    SAVED_OBJECT_GRAPH_HASH_FIELD_NUMBER: builtins.int
    CHECKPOINT_HASH_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    graph_def_checksum: builtins.int
    """Hash of the graph_def, referred to as a "checksum"."""
    graph_def_program_hash: builtins.int
    """Hash of regularized graph_def."""
    signature_def_hash: builtins.int
    """Hash of the regularized (sorted) SignatureDefs."""
    saved_object_graph_hash: builtins.int
    """Hash of the regularized SavedObjectGraph."""
    checkpoint_hash: builtins.int
    """Hash of the checkpoint."""
    @property
    def version(self) -> tensorflow.core.framework.versions_pb2.VersionDef:
        """Version specification of the fingerprint."""
    def __init__(
        self,
        *,
        graph_def_checksum: builtins.int | None = ...,
        graph_def_program_hash: builtins.int | None = ...,
        signature_def_hash: builtins.int | None = ...,
        saved_object_graph_hash: builtins.int | None = ...,
        checkpoint_hash: builtins.int | None = ...,
        version: tensorflow.core.framework.versions_pb2.VersionDef | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["checkpoint_hash", b"checkpoint_hash", "graph_def_checksum", b"graph_def_checksum", "graph_def_program_hash", b"graph_def_program_hash", "saved_object_graph_hash", b"saved_object_graph_hash", "signature_def_hash", b"signature_def_hash", "version", b"version"]) -> None: ...

global___FingerprintDef = FingerprintDef
