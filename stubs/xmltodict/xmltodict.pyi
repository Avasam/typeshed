from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from collections import OrderedDict
from collections.abc import Mapping
from types import GeneratorType
from typing import Any, overload
from typing_extensions import Final

__author__: Final[str]
__version__: Final[str]
__license__: Final[str]

class ParsingInterrupted(Exception): ...

def parse(
    xml_input: str | ReadableBuffer | SupportsRead[bytes] | GeneratorType[ReadableBuffer, Any, Any],
    encoding: str | None = ...,
    expat: Any = ...,
    process_namespaces: bool = ...,
    namespace_separator: str = ...,
    disable_entities: bool = ...,
    process_comments: bool = ...,
    **kwargs: Any,
) -> OrderedDict[str, Any]: ...
@overload
def unparse(
    input_dict: Mapping[str, Any],
    output: SupportsWrite[bytes] | SupportsWrite[str],
    encoding: str = ...,
    full_document: bool = ...,
    short_empty_elements: bool = ...,
    **kwargs: Any,
) -> None: ...
@overload
def unparse(
    input_dict: Mapping[str, Any],
    output: None = ...,
    encoding: str = ...,
    full_document: bool = ...,
    short_empty_elements: bool = ...,
    **kwargs: Any,
) -> str: ...
