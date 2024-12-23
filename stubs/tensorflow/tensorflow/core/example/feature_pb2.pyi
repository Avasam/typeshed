"""@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Protocol messages for describing features for machine learning model
training or inference.

There are three base Feature types:
  - bytes
  - float
  - int64

A Feature contains Lists which may hold zero or more values.  These
lists are the base values BytesList, FloatList, Int64List.

Features are organized into categories by name.  The Features message
contains the mapping from name to Feature.

Example Features for a movie recommendation application:
  feature {
    key: "age"
    value { float_list {
      value: 29.0
    }}
  }
  feature {
    key: "movie"
    value { bytes_list {
      value: "The Shawshank Redemption"
      value: "Fight Club"
    }}
  }
  feature {
    key: "movie_ratings"
    value { float_list {
      value: 9.0
      value: 9.7
    }}
  }
  feature {
    key: "suggestion"
    value { bytes_list {
      value: "Inception"
    }}
  }
  feature {
    key: "suggestion_purchased"
    value { int64_list {
      value: 1
    }}
  }
  feature {
    key: "purchase_price"
    value { float_list {
      value: 9.99
    }}
  }
"""

import builtins
import collections.abc
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BytesList(google.protobuf.message.Message):
    """LINT.IfChange
    Containers to hold repeated fundamental values.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(
        self,
        *,
        value: collections.abc.Iterable[builtins.bytes] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___BytesList = BytesList

@typing.final
class FloatList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        value: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___FloatList = FloatList

@typing.final
class Int64List(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        value: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___Int64List = Int64List

@typing.final
class Feature(google.protobuf.message.Message):
    """Containers for non-sequential data."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BYTES_LIST_FIELD_NUMBER: builtins.int
    FLOAT_LIST_FIELD_NUMBER: builtins.int
    INT64_LIST_FIELD_NUMBER: builtins.int
    @property
    def bytes_list(self) -> global___BytesList: ...
    @property
    def float_list(self) -> global___FloatList: ...
    @property
    def int64_list(self) -> global___Int64List: ...
    def __init__(
        self,
        *,
        bytes_list: global___BytesList | None = ...,
        float_list: global___FloatList | None = ...,
        int64_list: global___Int64List | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["bytes_list", b"bytes_list", "float_list", b"float_list", "int64_list", b"int64_list", "kind", b"kind"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bytes_list", b"bytes_list", "float_list", b"float_list", "int64_list", b"int64_list", "kind", b"kind"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["kind", b"kind"]) -> typing.Literal["bytes_list", "float_list", "int64_list"] | None: ...

global___Feature = Feature

@typing.final
class Features(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FeatureEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Feature: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___Feature | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FEATURE_FIELD_NUMBER: builtins.int
    @property
    def feature(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Feature]:
        """Map from feature name to feature."""

    def __init__(
        self,
        *,
        feature: collections.abc.Mapping[builtins.str, global___Feature] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature", b"feature"]) -> None: ...

global___Features = Features

@typing.final
class FeatureList(google.protobuf.message.Message):
    """Containers for sequential data.

    A FeatureList contains lists of Features.  These may hold zero or more
    Feature values.

    FeatureLists are organized into categories by name.  The FeatureLists message
    contains the mapping from name to FeatureList.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURE_FIELD_NUMBER: builtins.int
    @property
    def feature(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Feature]: ...
    def __init__(
        self,
        *,
        feature: collections.abc.Iterable[global___Feature] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature", b"feature"]) -> None: ...

global___FeatureList = FeatureList

@typing.final
class FeatureLists(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class FeatureListEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___FeatureList: ...
        def __init__(
            self,
            *,
            key: builtins.str | None = ...,
            value: global___FeatureList | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FEATURE_LIST_FIELD_NUMBER: builtins.int
    @property
    def feature_list(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___FeatureList]:
        """Map from feature name to feature list."""

    def __init__(
        self,
        *,
        feature_list: collections.abc.Mapping[builtins.str, global___FeatureList] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["feature_list", b"feature_list"]) -> None: ...

global___FeatureLists = FeatureLists
