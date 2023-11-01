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
import tensorflow.core.framework.attr_value_pb2
import tensorflow.core.framework.full_type_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class NodeDef(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class AttrEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> tensorflow.core.framework.attr_value_pb2.AttrValue: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: tensorflow.core.framework.attr_value_pb2.AttrValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class ExperimentalDebugInfo(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ORIGINAL_NODE_NAMES_FIELD_NUMBER: builtins.int
        ORIGINAL_FUNC_NAMES_FIELD_NUMBER: builtins.int
        @property
        def original_node_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """Opaque string inserted into error messages created by the runtime.

            This is intended to store the list of names of the nodes from the
            original graph that this node was derived. For example if this node, say
            C, was result of a fusion of 2 nodes A and B, then 'original_node' would
            be {A, B}. This information can be used to map errors originating at the
            current node to some top level source code.
            """
        @property
        def original_func_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
            """This is intended to store the list of names of the functions from the
            original graph that this node was derived. For example if this node, say
            C, was result of a fusion of node A in function FA and node B in function
            FB, then `original_funcs` would be {FA, FB}. If the node is in the top
            level graph, the `original_func` is empty. This information, with the
            `original_node_names` can be used to map errors originating at the
            current ndoe to some top level source code.
            """
        def __init__(
            self,
            *,
            original_node_names: collections.abc.Iterable[builtins.str] | None = ...,
            original_func_names: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["original_func_names", b"original_func_names", "original_node_names", b"original_node_names"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    OP_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    ATTR_FIELD_NUMBER: builtins.int
    EXPERIMENTAL_DEBUG_INFO_FIELD_NUMBER: builtins.int
    EXPERIMENTAL_TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name given to this operator. Used for naming inputs,
    logging, visualization, etc.  Unique within a single GraphDef.
    Must match the regexp "[A-Za-z0-9.][A-Za-z0-9_>./]*".
    """
    op: builtins.str
    """The operation name.  There may be custom parameters in attrs.
    Op names starting with an underscore are reserved for internal use.
    """
    @property
    def input(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Each input is "node:src_output" with "node" being a string name and
        "src_output" indicating which output tensor to use from "node". If
        "src_output" is 0 the ":0" suffix can be omitted.  Regular inputs
        may optionally be followed by control inputs that have the format
        "^node".
        """
    device: builtins.str
    """A (possibly partial) specification for the device on which this
    node should be placed.
    The expected syntax for this string is as follows:

    DEVICE_SPEC ::= PARTIAL_SPEC

    PARTIAL_SPEC ::= ("/" CONSTRAINT) *
    CONSTRAINT ::= ("job:" JOB_NAME)
                 | ("replica:" [1-9][0-9]*)
                 | ("task:" [1-9][0-9]*)
                 | ("device:" [A-Za-z]* ":" ([1-9][0-9]* | "*") )

    Valid values for this string include:
    * "/job:worker/replica:0/task:1/device:GPU:3"  (full specification)
    * "/job:worker/device:GPU:3"                   (partial specification)
    * ""                                    (no specification)

    If the constraints do not resolve to a single device (or if this
    field is empty or not present), the runtime will attempt to
    choose a device automatically.
    """
    @property
    def attr(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue]:
        """Operation-specific graph-construction-time configuration.
        Note that this should include all attrs defined in the
        corresponding OpDef, including those with a value matching
        the default -- this allows the default to change and makes
        NodeDefs easier to interpret on their own.  However, if
        an attr with a default is not specified in this list, the
        default will be used.
        The "names" (keys) must match the regexp "[a-z][a-z0-9_]+" (and
        one of the names from the corresponding OpDef's attr field).
        The values must have a type matching the corresponding OpDef
        attr's type field.
        TODO(josh11b): Add some examples here showing best practices.
        """
    @property
    def experimental_debug_info(self) -> global___NodeDef.ExperimentalDebugInfo:
        """This stores debug information associated with the node."""
    @property
    def experimental_type(self) -> tensorflow.core.framework.full_type_pb2.FullTypeDef:
        """The complete type of this node. Experimental and subject to change.
        Currently, the field only contains the return types of the node. That will
        extend in the future to contain the entire signature of the node, as a
        function type.
        """
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        op: builtins.str | None = ...,
        input: collections.abc.Iterable[builtins.str] | None = ...,
        device: builtins.str | None = ...,
        attr: collections.abc.Mapping[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue] | None = ...,
        experimental_debug_info: global___NodeDef.ExperimentalDebugInfo | None = ...,
        experimental_type: tensorflow.core.framework.full_type_pb2.FullTypeDef | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["experimental_debug_info", b"experimental_debug_info", "experimental_type", b"experimental_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["attr", b"attr", "device", b"device", "experimental_debug_info", b"experimental_debug_info", "experimental_type", b"experimental_type", "input", b"input", "name", b"name", "op", b"op"]) -> None: ...

global___NodeDef = NodeDef
