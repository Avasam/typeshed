"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol messages for describing the configuration of the ExampleParserOp.
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
class VarLenFeatureProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    VALUES_OUTPUT_TENSOR_NAME_FIELD_NUMBER: builtins.int
    INDICES_OUTPUT_TENSOR_NAME_FIELD_NUMBER: builtins.int
    SHAPES_OUTPUT_TENSOR_NAME_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    values_output_tensor_name: builtins.str
    indices_output_tensor_name: builtins.str
    shapes_output_tensor_name: builtins.str
    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        values_output_tensor_name: builtins.str | None = ...,
        indices_output_tensor_name: builtins.str | None = ...,
        shapes_output_tensor_name: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dtype", b"dtype", "indices_output_tensor_name", b"indices_output_tensor_name", "shapes_output_tensor_name", b"shapes_output_tensor_name", "values_output_tensor_name", b"values_output_tensor_name"]) -> None: ...

global___VarLenFeatureProto = VarLenFeatureProto

@typing.final
class FixedLenFeatureProto(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DTYPE_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    DEFAULT_VALUE_FIELD_NUMBER: builtins.int
    VALUES_OUTPUT_TENSOR_NAME_FIELD_NUMBER: builtins.int
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    values_output_tensor_name: builtins.str
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    @property
    def default_value(self) -> tensorflow.core.framework.tensor_pb2.TensorProto: ...
    def __init__(
        self,
        *,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        default_value: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
        values_output_tensor_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["default_value", b"default_value", "shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["default_value", b"default_value", "dtype", b"dtype", "shape", b"shape", "values_output_tensor_name", b"values_output_tensor_name"]) -> None: ...

global___FixedLenFeatureProto = FixedLenFeatureProto

@typing.final
class FeatureConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIXED_LEN_FEATURE_FIELD_NUMBER: builtins.int
    VAR_LEN_FEATURE_FIELD_NUMBER: builtins.int
    @property
    def fixed_len_feature(self) -> global___FixedLenFeatureProto: ...
    @property
    def var_len_feature(self) -> global___VarLenFeatureProto: ...
    def __init__(
        self,
        *,
        fixed_len_feature: global___FixedLenFeatureProto | None = ...,
        var_len_feature: global___VarLenFeatureProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["config", b"config", "fixed_len_feature", b"fixed_len_feature", "var_len_feature", b"var_len_feature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["config", b"config", "fixed_len_feature", b"fixed_len_feature", "var_len_feature", b"var_len_feature"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["config", b"config"]) -> typing.Literal["fixed_len_feature", "var_len_feature"] | None: ...

global___FeatureConfiguration = FeatureConfiguration

@typing.final
class ExampleParserConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FeatureMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___FeatureConfiguration: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___FeatureConfiguration | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FEATURE_MAP_FIELD_NUMBER: builtins.int
    @property
    def feature_map(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___FeatureConfiguration]: ...
    def __init__(
        self,
        *,
        feature_map: collections.abc.Mapping[builtins.str, global___FeatureConfiguration] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature_map", b"feature_map"]) -> None: ...

global___ExampleParserConfiguration = ExampleParserConfiguration
