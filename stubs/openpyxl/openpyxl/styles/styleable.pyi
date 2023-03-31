from _typeshed import Incomplete
from warnings import warn as warn

from .proxy import StyleProxy

class StyleDescriptor:
    collection: str
    key: str
    def __init__(self, collection: str, key: str) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls) -> StyleProxy: ...

class NumberFormatDescriptor:
    key: str
    collection: str
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class NamedStyleDescriptor:
    key: str
    collection: str
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class StyleArrayDescriptor:
    key: str
    def __init__(self, key: str) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls) -> bool: ...

class StyleableObject:
    font: StyleDescriptor
    fill: StyleDescriptor
    border: StyleDescriptor
    number_format: NumberFormatDescriptor
    protection: StyleDescriptor
    alignment: StyleDescriptor
    style: NamedStyleDescriptor
    quotePrefix: StyleArrayDescriptor
    pivotButton: StyleArrayDescriptor
    parent: Incomplete
    def __init__(self, sheet, style_array: Incomplete | None = None) -> None: ...
    @property
    def style_id(self) -> int: ...
    @property
    def has_style(self) -> bool: ...
