"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2022 The OpenXLA Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================
"""

import builtins
import typing

import google.protobuf.descriptor
import google.protobuf.message

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TestCompilationEnvironment1(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOME_FLAG_FIELD_NUMBER: builtins.int
    some_flag: builtins.int
    def __init__(self, *, some_flag: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["some_flag", b"some_flag"]) -> None: ...

global___TestCompilationEnvironment1 = TestCompilationEnvironment1

@typing.final
class TestCompilationEnvironment2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOME_OTHER_FLAG_FIELD_NUMBER: builtins.int
    some_other_flag: builtins.int
    def __init__(self, *, some_other_flag: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["some_other_flag", b"some_other_flag"]) -> None: ...

global___TestCompilationEnvironment2 = TestCompilationEnvironment2

@typing.final
class TestCompilationEnvironment3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    A_THIRD_FLAG_FIELD_NUMBER: builtins.int
    a_third_flag: builtins.int
    def __init__(self, *, a_third_flag: builtins.int | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["a_third_flag", b"a_third_flag"]) -> None: ...

global___TestCompilationEnvironment3 = TestCompilationEnvironment3
