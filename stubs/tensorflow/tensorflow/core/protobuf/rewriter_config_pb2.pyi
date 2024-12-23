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
import tensorflow.core.framework.attr_value_pb2
import tensorflow.core.protobuf.verifier_config_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AutoParallelOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLE_FIELD_NUMBER: builtins.int
    NUM_REPLICAS_FIELD_NUMBER: builtins.int
    enable: builtins.bool
    num_replicas: builtins.int
    def __init__(
        self,
        *,
        enable: builtins.bool | None = ...,
        num_replicas: builtins.int | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["enable", b"enable", "num_replicas", b"num_replicas"]) -> None: ...

global___AutoParallelOptions = AutoParallelOptions

@typing.final
class ScopedAllocatorOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENABLE_OP_FIELD_NUMBER: builtins.int
    @property
    def enable_op(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """If present, only perform optimization for these ops."""

    def __init__(
        self,
        *,
        enable_op: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["enable_op", b"enable_op"]) -> None: ...

global___ScopedAllocatorOptions = ScopedAllocatorOptions

@typing.final
class RewriterConfig(google.protobuf.message.Message):
    """Graph rewriting is experimental and subject to change, not covered by any
    API stability guarantees.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Toggle:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ToggleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RewriterConfig._Toggle.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT: RewriterConfig._Toggle.ValueType  # 0
        ON: RewriterConfig._Toggle.ValueType  # 1
        OFF: RewriterConfig._Toggle.ValueType  # 2
        AGGRESSIVE: RewriterConfig._Toggle.ValueType  # 3
        """Enable some aggressive optimizations that use assumptions that TF graphs
        may break. For example, assume the shape of a placeholder matches its
        actual feed.
        """
        EXPERIMENTAL_MLIR: RewriterConfig._Toggle.ValueType  # 4
        """Run MLIR pass if there's one implemented in TFG, do nothing otherwise.
        I.e., if there's no corresponding TFG pass, it's an OFF. This is supposed
        to be mapped with `ON` and there's no `AGGRESSIVE` in MLIR pass now.
        """
        EXPERIMENTAL_BOTH: RewriterConfig._Toggle.ValueType  # 5
        """Run both MLIR and Grappler passes consecutively and MLIR pass will come
        first.
        """

    class Toggle(_Toggle, metaclass=_ToggleEnumTypeWrapper):
        """Configuration options for the meta-optimizer. Unless otherwise noted, these
        configuration options do not apply to explicitly triggered optimization
        passes in the optimizers field.
        """

    DEFAULT: RewriterConfig.Toggle.ValueType  # 0
    ON: RewriterConfig.Toggle.ValueType  # 1
    OFF: RewriterConfig.Toggle.ValueType  # 2
    AGGRESSIVE: RewriterConfig.Toggle.ValueType  # 3
    """Enable some aggressive optimizations that use assumptions that TF graphs
    may break. For example, assume the shape of a placeholder matches its
    actual feed.
    """
    EXPERIMENTAL_MLIR: RewriterConfig.Toggle.ValueType  # 4
    """Run MLIR pass if there's one implemented in TFG, do nothing otherwise.
    I.e., if there's no corresponding TFG pass, it's an OFF. This is supposed
    to be mapped with `ON` and there's no `AGGRESSIVE` in MLIR pass now.
    """
    EXPERIMENTAL_BOTH: RewriterConfig.Toggle.ValueType  # 5
    """Run both MLIR and Grappler passes consecutively and MLIR pass will come
    first.
    """

    class _CpuLayout:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _CpuLayoutEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RewriterConfig._CpuLayout.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NO_CONVERSION_ON_CPU: RewriterConfig._CpuLayout.ValueType  # 0
        NCHW_TO_NHWC: RewriterConfig._CpuLayout.ValueType  # 1
        NHWC_TO_NCHW: RewriterConfig._CpuLayout.ValueType  # 2

    class CpuLayout(_CpuLayout, metaclass=_CpuLayoutEnumTypeWrapper):
        """Enum for layout conversion between NCHW and NHWC on CPU. Default is OFF."""

    NO_CONVERSION_ON_CPU: RewriterConfig.CpuLayout.ValueType  # 0
    NCHW_TO_NHWC: RewriterConfig.CpuLayout.ValueType  # 1
    NHWC_TO_NCHW: RewriterConfig.CpuLayout.ValueType  # 2

    class _NumIterationsType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _NumIterationsTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RewriterConfig._NumIterationsType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT_NUM_ITERS: RewriterConfig._NumIterationsType.ValueType  # 0
        ONE: RewriterConfig._NumIterationsType.ValueType  # 1
        TWO: RewriterConfig._NumIterationsType.ValueType  # 2

    class NumIterationsType(_NumIterationsType, metaclass=_NumIterationsTypeEnumTypeWrapper):
        """Enum controlling the number of times to run optimizers. The default is to
        run them twice.
        """

    DEFAULT_NUM_ITERS: RewriterConfig.NumIterationsType.ValueType  # 0
    ONE: RewriterConfig.NumIterationsType.ValueType  # 1
    TWO: RewriterConfig.NumIterationsType.ValueType  # 2

    class _MemOptType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MemOptTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RewriterConfig._MemOptType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEFAULT_MEM_OPT: RewriterConfig._MemOptType.ValueType  # 0
        """The default setting (SCHEDULING and SWAPPING HEURISTICS only)"""
        NO_MEM_OPT: RewriterConfig._MemOptType.ValueType  # 1
        """Disabled in the meta-optimizer."""
        MANUAL: RewriterConfig._MemOptType.ValueType  # 2
        """Driven by manual op-level annotations."""
        SWAPPING_HEURISTICS: RewriterConfig._MemOptType.ValueType  # 4
        """Driven by heuristics. The behavior of these heuristics is subject to
        change. Currently includes an experimental recomputation and swapping
        heuristics. Manual annotations are respected, but additional nodes are
        selected automatically.

        Swapping heuristic will move a tensor from the GPU to the CPU and move
        it back when needed to reduce peak memory usage.
        """
        RECOMPUTATION_HEURISTICS: RewriterConfig._MemOptType.ValueType  # 5
        """Recomputation heuristics will recompute ops (such as Relu activation)
        during backprop instead of storing them, reducing peak memory usage.
        """
        SCHEDULING_HEURISTICS: RewriterConfig._MemOptType.ValueType  # 6
        """Scheduling will split big ops such as AddN and try to enforce a schedule
        of the new computations that decreases peak memory usage.
        """
        HEURISTICS: RewriterConfig._MemOptType.ValueType  # 3
        """Use any combination of swapping and recomputation heuristics."""

    class MemOptType(_MemOptType, metaclass=_MemOptTypeEnumTypeWrapper): ...
    DEFAULT_MEM_OPT: RewriterConfig.MemOptType.ValueType  # 0
    """The default setting (SCHEDULING and SWAPPING HEURISTICS only)"""
    NO_MEM_OPT: RewriterConfig.MemOptType.ValueType  # 1
    """Disabled in the meta-optimizer."""
    MANUAL: RewriterConfig.MemOptType.ValueType  # 2
    """Driven by manual op-level annotations."""
    SWAPPING_HEURISTICS: RewriterConfig.MemOptType.ValueType  # 4
    """Driven by heuristics. The behavior of these heuristics is subject to
    change. Currently includes an experimental recomputation and swapping
    heuristics. Manual annotations are respected, but additional nodes are
    selected automatically.

    Swapping heuristic will move a tensor from the GPU to the CPU and move
    it back when needed to reduce peak memory usage.
    """
    RECOMPUTATION_HEURISTICS: RewriterConfig.MemOptType.ValueType  # 5
    """Recomputation heuristics will recompute ops (such as Relu activation)
    during backprop instead of storing them, reducing peak memory usage.
    """
    SCHEDULING_HEURISTICS: RewriterConfig.MemOptType.ValueType  # 6
    """Scheduling will split big ops such as AddN and try to enforce a schedule
    of the new computations that decreases peak memory usage.
    """
    HEURISTICS: RewriterConfig.MemOptType.ValueType  # 3
    """Use any combination of swapping and recomputation heuristics."""

    @typing.final
    class CustomGraphOptimizer(google.protobuf.message.Message):
        """Message to describe custom graph optimizer and its parameters"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing.final
        class ParameterMapEntry(google.protobuf.message.Message):
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
            def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

        NAME_FIELD_NUMBER: builtins.int
        PARAMETER_MAP_FIELD_NUMBER: builtins.int
        name: builtins.str
        @property
        def parameter_map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue]: ...
        def __init__(
            self,
            *,
            name: builtins.str | None = ...,
            parameter_map: collections.abc.Mapping[builtins.str, tensorflow.core.framework.attr_value_pb2.AttrValue] | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["name", b"name", "parameter_map", b"parameter_map"]) -> None: ...

    CPU_LAYOUT_CONVERSION_FIELD_NUMBER: builtins.int
    LAYOUT_OPTIMIZER_FIELD_NUMBER: builtins.int
    CONSTANT_FOLDING_FIELD_NUMBER: builtins.int
    SHAPE_OPTIMIZATION_FIELD_NUMBER: builtins.int
    REMAPPING_FIELD_NUMBER: builtins.int
    COMMON_SUBGRAPH_ELIMINATION_FIELD_NUMBER: builtins.int
    ARITHMETIC_OPTIMIZATION_FIELD_NUMBER: builtins.int
    DEPENDENCY_OPTIMIZATION_FIELD_NUMBER: builtins.int
    LOOP_OPTIMIZATION_FIELD_NUMBER: builtins.int
    FUNCTION_OPTIMIZATION_FIELD_NUMBER: builtins.int
    DEBUG_STRIPPER_FIELD_NUMBER: builtins.int
    DISABLE_MODEL_PRUNING_FIELD_NUMBER: builtins.int
    SCOPED_ALLOCATOR_OPTIMIZATION_FIELD_NUMBER: builtins.int
    PIN_TO_HOST_OPTIMIZATION_FIELD_NUMBER: builtins.int
    IMPLEMENTATION_SELECTOR_FIELD_NUMBER: builtins.int
    AUTO_MIXED_PRECISION_FIELD_NUMBER: builtins.int
    AUTO_MIXED_PRECISION_MKL_FIELD_NUMBER: builtins.int
    AUTO_MIXED_PRECISION_ONEDNN_BFLOAT16_FIELD_NUMBER: builtins.int
    AUTO_MIXED_PRECISION_CPU_FIELD_NUMBER: builtins.int
    DISABLE_META_OPTIMIZER_FIELD_NUMBER: builtins.int
    DISABLE_TFG_OPTIMIZER_FIELD_NUMBER: builtins.int
    USE_PLUGIN_OPTIMIZERS_FIELD_NUMBER: builtins.int
    EXPERIMENTAL_CONDITIONAL_CODE_MOTION_FIELD_NUMBER: builtins.int
    META_OPTIMIZER_ITERATIONS_FIELD_NUMBER: builtins.int
    MIN_GRAPH_NODES_FIELD_NUMBER: builtins.int
    EXPERIMENTAL_DISABLE_COMPRESSED_TENSOR_OPTIMIZATION_FIELD_NUMBER: builtins.int
    EXPERIMENTAL_DISABLE_FOLDING_QUANTIZATION_EMULATION_FIELD_NUMBER: builtins.int
    MEMORY_OPTIMIZATION_FIELD_NUMBER: builtins.int
    MEMORY_OPTIMIZER_TARGET_NODE_NAME_SCOPE_FIELD_NUMBER: builtins.int
    META_OPTIMIZER_TIMEOUT_MS_FIELD_NUMBER: builtins.int
    AUTO_PARALLEL_FIELD_NUMBER: builtins.int
    FAIL_ON_OPTIMIZER_ERRORS_FIELD_NUMBER: builtins.int
    SCOPED_ALLOCATOR_OPTS_FIELD_NUMBER: builtins.int
    OPTIMIZERS_FIELD_NUMBER: builtins.int
    CUSTOM_OPTIMIZERS_FIELD_NUMBER: builtins.int
    INTER_OPTIMIZER_VERIFIER_CONFIG_FIELD_NUMBER: builtins.int
    POST_OPTIMIZATION_VERIFIER_CONFIG_FIELD_NUMBER: builtins.int
    cpu_layout_conversion: global___RewriterConfig.CpuLayout.ValueType
    """CPU Conversion settings between NHCW and NCHW."""
    layout_optimizer: global___RewriterConfig.Toggle.ValueType
    """Optimize tensor layouts (default is ON)
    e.g. This will try to use NCHW layout on GPU which is faster.
    """
    constant_folding: global___RewriterConfig.Toggle.ValueType
    """Fold constants (default is ON)
    Statically infer the value of tensors when possible, and materialize the
    result using constants.
    """
    shape_optimization: global___RewriterConfig.Toggle.ValueType
    """Shape optimizations (default is ON)
    Simplify computations made on shapes.
    """
    remapping: global___RewriterConfig.Toggle.ValueType
    """Remapping (default is ON)
    Remap subgraphs onto more efficient implementations.
    """
    common_subgraph_elimination: global___RewriterConfig.Toggle.ValueType
    """Common subgraph elimination (default is ON)
    e.g. Simplify arithmetic ops; merge ops with same value (like constants).
    """
    arithmetic_optimization: global___RewriterConfig.Toggle.ValueType
    """Arithmetic optimizations (default is ON)
    e.g. Simplify arithmetic ops; merge ops with same value (like constants).
    """
    dependency_optimization: global___RewriterConfig.Toggle.ValueType
    """Control dependency optimizations (default is ON).
    Remove redundant control dependencies, which may enable other optimization.
    """
    loop_optimization: global___RewriterConfig.Toggle.ValueType
    """Loop optimizations (default is ON)."""
    function_optimization: global___RewriterConfig.Toggle.ValueType
    """Function optimizations (default is ON)."""
    debug_stripper: global___RewriterConfig.Toggle.ValueType
    """Strips debug-related nodes from the graph (off by default)."""
    disable_model_pruning: builtins.bool
    """If true, don't remove unnecessary ops from the graph"""
    scoped_allocator_optimization: global___RewriterConfig.Toggle.ValueType
    """Try to allocate some independent Op outputs contiguously in order to
    merge or eliminate downstream Ops (off by default).
    """
    pin_to_host_optimization: global___RewriterConfig.Toggle.ValueType
    """Force small ops onto the CPU (default is OFF)."""
    implementation_selector: global___RewriterConfig.Toggle.ValueType
    """Enable the swap of kernel implementations based on the device placement
    (default is ON).
    """
    auto_mixed_precision: global___RewriterConfig.Toggle.ValueType
    """Optimize data types for CUDA/oneDNN (default is OFF).
    This will try to use float16 on GPU/CPU which is faster.
    Note that this can change the numerical stability of the graph and may
    require the use of loss scaling to maintain model convergence.
    """
    auto_mixed_precision_mkl: global___RewriterConfig.Toggle.ValueType
    """Optimize data types for oneDNN (default is OFF).
    This will try to use bfloat16 on CPUs, which is faster.
    Note that this can change the numerical stability of the graph.
    Note: this is deprecated.
    It is replaced by auto_mixed_precision_onednn_bfloat16
    """
    auto_mixed_precision_onednn_bfloat16: global___RewriterConfig.Toggle.ValueType
    """Optimize data types for oneDNN (default is OFF).
    This will try to use bfloat16 on CPUs, which is faster.
    Note that this can change the numerical stability of the graph.
    Note: this is equivalent to the deprecated option auto_mixed_precision_mkl
    """
    auto_mixed_precision_cpu: global___RewriterConfig.Toggle.ValueType
    """Emulate a model using data type float16 on CPU (default is OFF).
    This will try to emulate the float16 inputs and outputs of an operator
    on CPU to have better correlation with float16 on GPU; however the
    computation in the operator is based on float32.
    Note that this can change the numerical stability of the graph.
    """
    disable_meta_optimizer: builtins.bool
    """Disable the entire meta optimizer (off by default)."""
    disable_tfg_optimizer: builtins.bool
    """Disable the TFG optimizer (off by default)."""
    use_plugin_optimizers: global___RewriterConfig.Toggle.ValueType
    """Optimizers registered by plugin (default is ON)"""
    experimental_conditional_code_motion: global___RewriterConfig.Toggle.ValueType
    """Conditional code motion (default is ON)."""
    meta_optimizer_iterations: global___RewriterConfig.NumIterationsType.ValueType
    """Controls how many times we run the optimizers in meta optimizer (default
    is once).
    """
    min_graph_nodes: builtins.int
    """The minimum number of nodes in a graph to optimizer. For smaller graphs,
    optimization is skipped.
    0 means the system picks an appropriate number.
    < 0 means do not skip optimization.
    """
    experimental_disable_compressed_tensor_optimization: builtins.bool
    """Disable optimizations that assume compressed tensors. Note that this flag
    is experimental and may be removed in the future.
    """
    experimental_disable_folding_quantization_emulation: builtins.bool
    """Disable folding quantization emulation ops such as FakeQuantWithMinMax* and
    QuantizeAndDequantize*. Some compilers (e.g. the TF-to-tflite converter)
    have to extract quantization configs (e.g. min/max range, number of bits,
    and per-channel) from the quantization emulation ops. Note that this flag
    is experimental and may be removed in the future. See b/174138564 for more
    details.
    """
    memory_optimization: global___RewriterConfig.MemOptType.ValueType
    """Configures memory optimization passes through the meta-optimizer. Has no
    effect on manually requested memory optimization passes in the optimizers
    field.
    """
    memory_optimizer_target_node_name_scope: builtins.str
    """A node name scope for node names which are valid outputs of recomputations.
    Inputs to nodes that match this scope may be recomputed (subject either to
    manual annotation of those input nodes or to manual annotation and
    heuristics depending on memory_optimization), but the nodes themselves will
    not be recomputed. This matches any sub-scopes as well, meaning the scope
    can appear not just as a top-level scope. For example, if the value is
    "gradients/", the default, it will match node name "gradients/foo",
    "foo/gradients/bar", but not "foo_gradients/"
    """
    meta_optimizer_timeout_ms: builtins.int
    """Maximum number of milliseconds to spend optimizing a single graph before
    timing out. If less than or equal to 0 (default value) the optimizer will
    never time out.
    """
    fail_on_optimizer_errors: builtins.bool
    """If true, any optimization pass failing will cause the MetaOptimizer to
    stop with an error. By default - or when set to false, failing passes are
    skipped silently.
    """
    @property
    def auto_parallel(self) -> global___AutoParallelOptions:
        """Configures AutoParallel optimization passes either through the
        meta-optimizer or when manually specified through the optimizers field.
        """

    @property
    def scoped_allocator_opts(self) -> global___ScopedAllocatorOptions: ...
    @property
    def optimizers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """If non-empty, will use this as an alternative way to specify a list of
        optimizations to turn on and the order of the optimizations (replacing the
        meta-optimizer).

        Of the RewriterConfig options, only the AutoParallel configuration options
        (the auto_parallel field) apply to manually requested optimization passes
        ("autoparallel"). Memory optimization passes ("memory") invoked here are
        not configurable (in contrast to memory optimization passes through the
        meta-optimizer) and act only on manual op annotations.

        Custom optimizers (see custom_optimizers) that are not part of this
        schedule will be run after - in the order that they were specified.
        """

    @property
    def custom_optimizers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RewriterConfig.CustomGraphOptimizer]:
        """List of CustomGraphOptimizers to apply."""

    @property
    def inter_optimizer_verifier_config(self) -> tensorflow.core.protobuf.verifier_config_pb2.VerifierConfig:
        """VerifierConfig specifying the verifiers to be run after every optimizer."""

    @property
    def post_optimization_verifier_config(self) -> tensorflow.core.protobuf.verifier_config_pb2.VerifierConfig:
        """VerifierConfig specifying the verifiers to be run at the end, after all
        optimizers have run.
        """

    def __init__(
        self,
        *,
        cpu_layout_conversion: global___RewriterConfig.CpuLayout.ValueType | None = ...,
        layout_optimizer: global___RewriterConfig.Toggle.ValueType | None = ...,
        constant_folding: global___RewriterConfig.Toggle.ValueType | None = ...,
        shape_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        remapping: global___RewriterConfig.Toggle.ValueType | None = ...,
        common_subgraph_elimination: global___RewriterConfig.Toggle.ValueType | None = ...,
        arithmetic_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        dependency_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        loop_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        function_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        debug_stripper: global___RewriterConfig.Toggle.ValueType | None = ...,
        disable_model_pruning: builtins.bool | None = ...,
        scoped_allocator_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        pin_to_host_optimization: global___RewriterConfig.Toggle.ValueType | None = ...,
        implementation_selector: global___RewriterConfig.Toggle.ValueType | None = ...,
        auto_mixed_precision: global___RewriterConfig.Toggle.ValueType | None = ...,
        auto_mixed_precision_mkl: global___RewriterConfig.Toggle.ValueType | None = ...,
        auto_mixed_precision_onednn_bfloat16: global___RewriterConfig.Toggle.ValueType | None = ...,
        auto_mixed_precision_cpu: global___RewriterConfig.Toggle.ValueType | None = ...,
        disable_meta_optimizer: builtins.bool | None = ...,
        disable_tfg_optimizer: builtins.bool | None = ...,
        use_plugin_optimizers: global___RewriterConfig.Toggle.ValueType | None = ...,
        experimental_conditional_code_motion: global___RewriterConfig.Toggle.ValueType | None = ...,
        meta_optimizer_iterations: global___RewriterConfig.NumIterationsType.ValueType | None = ...,
        min_graph_nodes: builtins.int | None = ...,
        experimental_disable_compressed_tensor_optimization: builtins.bool | None = ...,
        experimental_disable_folding_quantization_emulation: builtins.bool | None = ...,
        memory_optimization: global___RewriterConfig.MemOptType.ValueType | None = ...,
        memory_optimizer_target_node_name_scope: builtins.str | None = ...,
        meta_optimizer_timeout_ms: builtins.int | None = ...,
        auto_parallel: global___AutoParallelOptions | None = ...,
        fail_on_optimizer_errors: builtins.bool | None = ...,
        scoped_allocator_opts: global___ScopedAllocatorOptions | None = ...,
        optimizers: collections.abc.Iterable[builtins.str] | None = ...,
        custom_optimizers: collections.abc.Iterable[global___RewriterConfig.CustomGraphOptimizer] | None = ...,
        inter_optimizer_verifier_config: tensorflow.core.protobuf.verifier_config_pb2.VerifierConfig | None = ...,
        post_optimization_verifier_config: tensorflow.core.protobuf.verifier_config_pb2.VerifierConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["auto_parallel", b"auto_parallel", "inter_optimizer_verifier_config", b"inter_optimizer_verifier_config", "post_optimization_verifier_config", b"post_optimization_verifier_config", "scoped_allocator_opts", b"scoped_allocator_opts"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["arithmetic_optimization", b"arithmetic_optimization", "auto_mixed_precision", b"auto_mixed_precision", "auto_mixed_precision_cpu", b"auto_mixed_precision_cpu", "auto_mixed_precision_mkl", b"auto_mixed_precision_mkl", "auto_mixed_precision_onednn_bfloat16", b"auto_mixed_precision_onednn_bfloat16", "auto_parallel", b"auto_parallel", "common_subgraph_elimination", b"common_subgraph_elimination", "constant_folding", b"constant_folding", "cpu_layout_conversion", b"cpu_layout_conversion", "custom_optimizers", b"custom_optimizers", "debug_stripper", b"debug_stripper", "dependency_optimization", b"dependency_optimization", "disable_meta_optimizer", b"disable_meta_optimizer", "disable_model_pruning", b"disable_model_pruning", "disable_tfg_optimizer", b"disable_tfg_optimizer", "experimental_conditional_code_motion", b"experimental_conditional_code_motion", "experimental_disable_compressed_tensor_optimization", b"experimental_disable_compressed_tensor_optimization", "experimental_disable_folding_quantization_emulation", b"experimental_disable_folding_quantization_emulation", "fail_on_optimizer_errors", b"fail_on_optimizer_errors", "function_optimization", b"function_optimization", "implementation_selector", b"implementation_selector", "inter_optimizer_verifier_config", b"inter_optimizer_verifier_config", "layout_optimizer", b"layout_optimizer", "loop_optimization", b"loop_optimization", "memory_optimization", b"memory_optimization", "memory_optimizer_target_node_name_scope", b"memory_optimizer_target_node_name_scope", "meta_optimizer_iterations", b"meta_optimizer_iterations", "meta_optimizer_timeout_ms", b"meta_optimizer_timeout_ms", "min_graph_nodes", b"min_graph_nodes", "optimizers", b"optimizers", "pin_to_host_optimization", b"pin_to_host_optimization", "post_optimization_verifier_config", b"post_optimization_verifier_config", "remapping", b"remapping", "scoped_allocator_optimization", b"scoped_allocator_optimization", "scoped_allocator_opts", b"scoped_allocator_opts", "shape_optimization", b"shape_optimization", "use_plugin_optimizers", b"use_plugin_optimizers"]) -> None: ...

global___RewriterConfig = RewriterConfig
