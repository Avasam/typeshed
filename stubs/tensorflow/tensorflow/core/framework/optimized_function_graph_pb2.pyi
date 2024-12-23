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
import tensorflow.core.framework.graph_pb2
import tensorflow.core.framework.types_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class OptimizedFunctionGraph(google.protobuf.message.Message):
    """Optimized function graph after instantiation-related graph optimization
    passes (up till before graph partitioning). The first half of the proto is
    representing a GraphDef and the rest of the fields are extra information from
    graph optimizations.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _OptimizationSource:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OptimizationSourceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[OptimizedFunctionGraph._OptimizationSource.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SOURCE_UNSPECIFIED: OptimizedFunctionGraph._OptimizationSource.ValueType  # 0
        AOT: OptimizedFunctionGraph._OptimizationSource.ValueType  # 1
        JIT: OptimizedFunctionGraph._OptimizationSource.ValueType  # 2

    class OptimizationSource(_OptimizationSource, metaclass=_OptimizationSourceEnumTypeWrapper):
        """Enum for distinguishing the origin where the proto is created.

        AOT: proto is created in ahead-of-time environment, which can be different
        from the environment where the graph is actually executed.

        JIT: proto is created in just-in-time execution, which has the same
        environment as the one the graph is actually executed.
        """

    SOURCE_UNSPECIFIED: OptimizedFunctionGraph.OptimizationSource.ValueType  # 0
    AOT: OptimizedFunctionGraph.OptimizationSource.ValueType  # 1
    JIT: OptimizedFunctionGraph.OptimizationSource.ValueType  # 2

    @typing.final
    class NodeNameToControlRetEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    FUNCTION_GRAPH_FIELD_NUMBER: builtins.int
    NODE_NAME_TO_CONTROL_RET_FIELD_NUMBER: builtins.int
    RET_TYPES_FIELD_NUMBER: builtins.int
    NUM_RETURN_NODES_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    OPTIMIZATION_TIME_USECS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Function name. It can be a human-readable SignatureDef's method name, or a
    FunctionDef name.
    """
    num_return_nodes: builtins.int
    """Number of return nodes. This is an output of graph preprocessing."""
    source: global___OptimizedFunctionGraph.OptimizationSource.ValueType
    """Indicates the source environment where this proto is generated."""
    optimization_time_usecs: builtins.int
    """Time (in microseconds) spent on running the graph optimization passes for
    this function.
    """
    @property
    def function_graph(self) -> tensorflow.core.framework.graph_pb2.GraphDef:
        """Optimized function graph."""

    @property
    def node_name_to_control_ret(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Maps from node name to control ret. This is an output from running TF/XLA
        bridge.
        """

    @property
    def ret_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[tensorflow.core.framework.types_pb2.DataType.ValueType]:
        """Return node types of the function. This is an output of graph
        preprocessing.
        """

    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        function_graph: tensorflow.core.framework.graph_pb2.GraphDef | None = ...,
        node_name_to_control_ret: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        ret_types: collections.abc.Iterable[tensorflow.core.framework.types_pb2.DataType.ValueType] | None = ...,
        num_return_nodes: builtins.int | None = ...,
        source: global___OptimizedFunctionGraph.OptimizationSource.ValueType | None = ...,
        optimization_time_usecs: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_optimization_time_usecs", b"_optimization_time_usecs", "_source", b"_source", "function_graph", b"function_graph", "optimization_time_usecs", b"optimization_time_usecs", "source", b"source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_optimization_time_usecs", b"_optimization_time_usecs", "_source", b"_source", "function_graph", b"function_graph", "name", b"name", "node_name_to_control_ret", b"node_name_to_control_ret", "num_return_nodes", b"num_return_nodes", "optimization_time_usecs", b"optimization_time_usecs", "ret_types", b"ret_types", "source", b"source"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_optimization_time_usecs", b"_optimization_time_usecs"]) -> typing.Literal["optimization_time_usecs"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_source", b"_source"]) -> typing.Literal["source"] | None: ...

global___OptimizedFunctionGraph = OptimizedFunctionGraph
