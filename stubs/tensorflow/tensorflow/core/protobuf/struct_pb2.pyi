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
import tensorflow.core.framework.tensor_pb2
import tensorflow.core.framework.tensor_shape_pb2
import tensorflow.core.framework.types_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class StructuredValue(google.protobuf.message.Message):
    """`StructuredValue` represents a dynamically typed value representing various
    data structures that are inspired by Python data structures typically used in
    TensorFlow functions as inputs and outputs.

    For example when saving a Layer there may be a `training` argument. If the
    user passes a boolean True/False, that switches between two concrete
    TensorFlow functions. In order to switch between them in the same way after
    loading the SavedModel, we need to represent "True" and "False".

    A more advanced example might be a function which takes a list of
    dictionaries mapping from strings to Tensors. In order to map from
    user-specified arguments `[{"a": tf.constant(1.)}, {"q": tf.constant(3.)}]`
    after load to the right saved TensorFlow function, we need to represent the
    nested structure and the strings, recording that we have a trace for anything
    matching `[{"a": tf.TensorSpec(None, tf.float32)}, {"q": tf.TensorSpec([],
    tf.float64)}]` as an example.

    Likewise functions may return nested structures of Tensors, for example
    returning a dictionary mapping from strings to Tensors. In order for the
    loaded function to return the same structure we need to serialize it.

    This is an ergonomic aid for working with loaded SavedModels, not a promise
    to serialize all possible function signatures. For example we do not expect
    to pickle generic Python objects, and ideally we'd stay language-agnostic.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NONE_VALUE_FIELD_NUMBER: builtins.int
    FLOAT64_VALUE_FIELD_NUMBER: builtins.int
    INT64_VALUE_FIELD_NUMBER: builtins.int
    STRING_VALUE_FIELD_NUMBER: builtins.int
    BOOL_VALUE_FIELD_NUMBER: builtins.int
    TENSOR_SHAPE_VALUE_FIELD_NUMBER: builtins.int
    TENSOR_DTYPE_VALUE_FIELD_NUMBER: builtins.int
    TENSOR_SPEC_VALUE_FIELD_NUMBER: builtins.int
    TYPE_SPEC_VALUE_FIELD_NUMBER: builtins.int
    BOUNDED_TENSOR_SPEC_VALUE_FIELD_NUMBER: builtins.int
    LIST_VALUE_FIELD_NUMBER: builtins.int
    TUPLE_VALUE_FIELD_NUMBER: builtins.int
    DICT_VALUE_FIELD_NUMBER: builtins.int
    NAMED_TUPLE_VALUE_FIELD_NUMBER: builtins.int
    TENSOR_VALUE_FIELD_NUMBER: builtins.int
    NUMPY_VALUE_FIELD_NUMBER: builtins.int
    float64_value: builtins.float
    """Represents a double-precision floating-point value (a Python `float`)."""
    int64_value: builtins.int
    """Represents a signed integer value, limited to 64 bits.
    Larger values from Python's arbitrary-precision integers are unsupported.
    """
    string_value: builtins.str
    """Represents a string of Unicode characters stored in a Python `str`.
    In Python 3, this is exactly what type `str` is.
    In Python 2, this is the UTF-8 encoding of the characters.
    For strings with ASCII characters only (as often used in TensorFlow code)
    there is effectively no difference between the language versions.
    The obsolescent `unicode` type of Python 2 is not supported here.
    """
    bool_value: builtins.bool
    """Represents a boolean value."""
    tensor_dtype_value: tensorflow.core.framework.types_pb2.DataType.ValueType
    """Represents an enum value for dtype."""
    @property
    def none_value(self) -> global___NoneValue:
        """Represents None."""

    @property
    def tensor_shape_value(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto:
        """Represents a TensorShape."""

    @property
    def tensor_spec_value(self) -> global___TensorSpecProto:
        """Represents a value for tf.TensorSpec."""

    @property
    def type_spec_value(self) -> global___TypeSpecProto:
        """Represents a value for tf.TypeSpec."""

    @property
    def bounded_tensor_spec_value(self) -> global___BoundedTensorSpecProto:
        """Represents a value for tf.BoundedTensorSpec."""

    @property
    def list_value(self) -> global___ListValue:
        """Represents a list of `Value`."""

    @property
    def tuple_value(self) -> global___TupleValue:
        """Represents a tuple of `Value`."""

    @property
    def dict_value(self) -> global___DictValue:
        """Represents a dict `Value`."""

    @property
    def named_tuple_value(self) -> global___NamedTupleValue:
        """Represents Python's namedtuple."""

    @property
    def tensor_value(self) -> tensorflow.core.framework.tensor_pb2.TensorProto:
        """Represents a value for tf.Tensor."""

    @property
    def numpy_value(self) -> tensorflow.core.framework.tensor_pb2.TensorProto:
        """Represents a value for np.ndarray."""

    def __init__(
        self,
        *,
        none_value: global___NoneValue | None = ...,
        float64_value: builtins.float | None = ...,
        int64_value: builtins.int | None = ...,
        string_value: builtins.str | None = ...,
        bool_value: builtins.bool | None = ...,
        tensor_shape_value: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        tensor_dtype_value: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        tensor_spec_value: global___TensorSpecProto | None = ...,
        type_spec_value: global___TypeSpecProto | None = ...,
        bounded_tensor_spec_value: global___BoundedTensorSpecProto | None = ...,
        list_value: global___ListValue | None = ...,
        tuple_value: global___TupleValue | None = ...,
        dict_value: global___DictValue | None = ...,
        named_tuple_value: global___NamedTupleValue | None = ...,
        tensor_value: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
        numpy_value: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bool_value", b"bool_value", "bounded_tensor_spec_value", b"bounded_tensor_spec_value", "dict_value", b"dict_value", "float64_value", b"float64_value", "int64_value", b"int64_value", "kind", b"kind", "list_value", b"list_value", "named_tuple_value", b"named_tuple_value", "none_value", b"none_value", "numpy_value", b"numpy_value", "string_value", b"string_value", "tensor_dtype_value", b"tensor_dtype_value", "tensor_shape_value", b"tensor_shape_value", "tensor_spec_value", b"tensor_spec_value", "tensor_value", b"tensor_value", "tuple_value", b"tuple_value", "type_spec_value", b"type_spec_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bool_value", b"bool_value", "bounded_tensor_spec_value", b"bounded_tensor_spec_value", "dict_value", b"dict_value", "float64_value", b"float64_value", "int64_value", b"int64_value", "kind", b"kind", "list_value", b"list_value", "named_tuple_value", b"named_tuple_value", "none_value", b"none_value", "numpy_value", b"numpy_value", "string_value", b"string_value", "tensor_dtype_value", b"tensor_dtype_value", "tensor_shape_value", b"tensor_shape_value", "tensor_spec_value", b"tensor_spec_value", "tensor_value", b"tensor_value", "tuple_value", b"tuple_value", "type_spec_value", b"type_spec_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["kind", b"kind"]) -> typing.Literal["none_value", "float64_value", "int64_value", "string_value", "bool_value", "tensor_shape_value", "tensor_dtype_value", "tensor_spec_value", "type_spec_value", "bounded_tensor_spec_value", "list_value", "tuple_value", "dict_value", "named_tuple_value", "tensor_value", "numpy_value"] | None: ...

global___StructuredValue = StructuredValue

@typing.final
class NoneValue(google.protobuf.message.Message):
    """Represents None."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___NoneValue = NoneValue

@typing.final
class ListValue(google.protobuf.message.Message):
    """Represents a Python list."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StructuredValue]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[global___StructuredValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["values", b"values"]) -> None: ...

global___ListValue = ListValue

@typing.final
class TupleValue(google.protobuf.message.Message):
    """Represents a Python tuple."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StructuredValue]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[global___StructuredValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["values", b"values"]) -> None: ...

global___TupleValue = TupleValue

@typing.final
class DictValue(google.protobuf.message.Message):
    """Represents a Python dict keyed by `str`.
    The comment on Unicode from Value.string_value applies analogously.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FieldsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___StructuredValue: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___StructuredValue | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___StructuredValue]: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Mapping[builtins.str, global___StructuredValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["fields", b"fields"]) -> None: ...

global___DictValue = DictValue

@typing.final
class PairValue(google.protobuf.message.Message):
    """Represents a (key, value) pair."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    @property
    def value(self) -> global___StructuredValue: ...
    def __init__(
        self,
        *,
        key: builtins.str | None = ...,
        value: global___StructuredValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

global___PairValue = PairValue

@typing.final
class NamedTupleValue(google.protobuf.message.Message):
    """Represents Python's namedtuple."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    name: builtins.str
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PairValue]: ...
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        values: collections.abc.Iterable[global___PairValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["name", b"name", "values", b"values"]) -> None: ...

global___NamedTupleValue = NamedTupleValue

@typing.final
class TensorSpecProto(google.protobuf.message.Message):
    """A protobuf to represent tf.TensorSpec."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dtype", b"dtype", "name", b"name", "shape", b"shape"]) -> None: ...

global___TensorSpecProto = TensorSpecProto

@typing.final
class BoundedTensorSpecProto(google.protobuf.message.Message):
    """A protobuf to represent tf.BoundedTensorSpec."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    SHAPE_FIELD_NUMBER: builtins.int
    DTYPE_FIELD_NUMBER: builtins.int
    MINIMUM_FIELD_NUMBER: builtins.int
    MAXIMUM_FIELD_NUMBER: builtins.int
    name: builtins.str
    dtype: tensorflow.core.framework.types_pb2.DataType.ValueType
    @property
    def shape(self) -> tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto: ...
    @property
    def minimum(self) -> tensorflow.core.framework.tensor_pb2.TensorProto: ...
    @property
    def maximum(self) -> tensorflow.core.framework.tensor_pb2.TensorProto: ...
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        shape: tensorflow.core.framework.tensor_shape_pb2.TensorShapeProto | None = ...,
        dtype: tensorflow.core.framework.types_pb2.DataType.ValueType | None = ...,
        minimum: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
        maximum: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["maximum", b"maximum", "minimum", b"minimum", "shape", b"shape"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dtype", b"dtype", "maximum", b"maximum", "minimum", b"minimum", "name", b"name", "shape", b"shape"]) -> None: ...

global___BoundedTensorSpecProto = BoundedTensorSpecProto

@typing.final
class TypeSpecProto(google.protobuf.message.Message):
    """Represents a tf.TypeSpec"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _TypeSpecClass:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeSpecClassEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[TypeSpecProto._TypeSpecClass.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNKNOWN: TypeSpecProto._TypeSpecClass.ValueType  # 0
        SPARSE_TENSOR_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 1
        """tf.SparseTensorSpec"""
        INDEXED_SLICES_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 2
        """tf.IndexedSlicesSpec"""
        RAGGED_TENSOR_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 3
        """tf.RaggedTensorSpec"""
        TENSOR_ARRAY_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 4
        """tf.TensorArraySpec"""
        DATA_DATASET_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 5
        """tf.data.DatasetSpec"""
        DATA_ITERATOR_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 6
        """IteratorSpec from data/ops/iterator_ops.py"""
        OPTIONAL_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 7
        """tf.OptionalSpec"""
        PER_REPLICA_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 8
        """PerReplicaSpec from distribute/values.py"""
        VARIABLE_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 9
        """tf.VariableSpec"""
        ROW_PARTITION_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 10
        """RowPartitionSpec from ragged/row_partition.py"""
        REGISTERED_TYPE_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 12
        """The type registered as type_spec_class_name."""
        EXTENSION_TYPE_SPEC: TypeSpecProto._TypeSpecClass.ValueType  # 13
        """Subclasses of tf.ExtensionType"""

    class TypeSpecClass(_TypeSpecClass, metaclass=_TypeSpecClassEnumTypeWrapper): ...
    UNKNOWN: TypeSpecProto.TypeSpecClass.ValueType  # 0
    SPARSE_TENSOR_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 1
    """tf.SparseTensorSpec"""
    INDEXED_SLICES_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 2
    """tf.IndexedSlicesSpec"""
    RAGGED_TENSOR_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 3
    """tf.RaggedTensorSpec"""
    TENSOR_ARRAY_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 4
    """tf.TensorArraySpec"""
    DATA_DATASET_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 5
    """tf.data.DatasetSpec"""
    DATA_ITERATOR_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 6
    """IteratorSpec from data/ops/iterator_ops.py"""
    OPTIONAL_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 7
    """tf.OptionalSpec"""
    PER_REPLICA_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 8
    """PerReplicaSpec from distribute/values.py"""
    VARIABLE_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 9
    """tf.VariableSpec"""
    ROW_PARTITION_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 10
    """RowPartitionSpec from ragged/row_partition.py"""
    REGISTERED_TYPE_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 12
    """The type registered as type_spec_class_name."""
    EXTENSION_TYPE_SPEC: TypeSpecProto.TypeSpecClass.ValueType  # 13
    """Subclasses of tf.ExtensionType"""

    TYPE_SPEC_CLASS_FIELD_NUMBER: builtins.int
    TYPE_STATE_FIELD_NUMBER: builtins.int
    TYPE_SPEC_CLASS_NAME_FIELD_NUMBER: builtins.int
    NUM_FLAT_COMPONENTS_FIELD_NUMBER: builtins.int
    type_spec_class: global___TypeSpecProto.TypeSpecClass.ValueType
    type_spec_class_name: builtins.str
    """The name of the TypeSpec class.
     * If type_spec_class == REGISTERED_TYPE_SPEC, the TypeSpec class is
       the one registered under this name. For types registered outside
       core TensorFlow by an add-on library, that library must be loaded
       before this value can be deserialized by nested_structure_coder.
     * If type_spec_class specifies a particular TypeSpec class, this field is
       redundant with the type_spec_class enum, and is only used for error
       reporting in older binaries that do not know the tupe_spec_class enum.
    """
    num_flat_components: builtins.int
    """The number of flat tensor components required by this TypeSpec."""
    @property
    def type_state(self) -> global___StructuredValue:
        """The value returned by TypeSpec._serialize()."""

    def __init__(
        self,
        *,
        type_spec_class: global___TypeSpecProto.TypeSpecClass.ValueType | None = ...,
        type_state: global___StructuredValue | None = ...,
        type_spec_class_name: builtins.str | None = ...,
        num_flat_components: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["type_state", b"type_state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["num_flat_components", b"num_flat_components", "type_spec_class", b"type_spec_class", "type_spec_class_name", b"type_spec_class_name", "type_state", b"type_state"]) -> None: ...

global___TypeSpecProto = TypeSpecProto
