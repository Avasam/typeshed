"""@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import tensorflow.core.framework.function_pb2
import tensorflow.core.framework.graph_debug_info_pb2
import tensorflow.core.framework.node_def_pb2
import tensorflow.core.framework.versions_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GraphDef(google.protobuf.message.Message):
    """Represents the graph of operations"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_FIELD_NUMBER: builtins.int
    VERSIONS_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    LIBRARY_FIELD_NUMBER: builtins.int
    DEBUG_INFO_FIELD_NUMBER: builtins.int
    version: builtins.int
    """Deprecated single version field; use versions above instead.  Since all
    GraphDef changes before "versions" was introduced were forward
    compatible, this field is entirely ignored.
    """
    @property
    def node(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tensorflow.core.framework.node_def_pb2.NodeDef]: ...
    @property
    def versions(self) -> tensorflow.core.framework.versions_pb2.VersionDef:
        """Compatibility versions of the graph.  See core/public/version.h for version
        history.  The GraphDef version is distinct from the TensorFlow version, and
        each release of TensorFlow will support a range of GraphDef versions.
        """

    @property
    def library(self) -> tensorflow.core.framework.function_pb2.FunctionDefLibrary:
        """"library" provides user-defined functions.

        Naming:
          * library.function.name are in a flat namespace.
            NOTE: We may need to change it to be hierarchical to support
            different orgs. E.g.,
            { "/google/nn", { ... }},
            { "/google/vision", { ... }}
            { "/org_foo/module_bar", { ... }}
            map<string, FunctionDefLib> named_lib;
          * If node[i].op is the name of one function in "library",
            node[i] is deemed as a function call. Otherwise, node[i].op
            must be a primitive operation supported by the runtime.


        Function call semantics:

          * The callee may start execution as soon as some of its inputs
            are ready. The caller may want to use Tuple() mechanism to
            ensure all inputs are ready in the same time.

          * The consumer of return values may start executing as soon as
            the return values the consumer depends on are ready.  The
            consumer may want to use Tuple() mechanism to ensure the
            consumer does not start until all return values of the callee
            function are ready.
        """

    @property
    def debug_info(self) -> tensorflow.core.framework.graph_debug_info_pb2.GraphDebugInfo:
        """Stack traces for the nodes in this graph."""

    def __init__(
        self,
        *,
        node: collections.abc.Iterable[tensorflow.core.framework.node_def_pb2.NodeDef] | None = ...,
        versions: tensorflow.core.framework.versions_pb2.VersionDef | None = ...,
        version: builtins.int | None = ...,
        library: tensorflow.core.framework.function_pb2.FunctionDefLibrary | None = ...,
        debug_info: tensorflow.core.framework.graph_debug_info_pb2.GraphDebugInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["debug_info", b"debug_info", "library", b"library", "versions", b"versions"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["debug_info", b"debug_info", "library", b"library", "node", b"node", "version", b"version", "versions", b"versions"]) -> None: ...

global___GraphDef = GraphDef
