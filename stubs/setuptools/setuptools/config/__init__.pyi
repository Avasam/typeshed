from _typeshed import Incomplete
from collections.abc import Callable
from typing import TypeVar

from . import setupcfg

Fn = TypeVar("Fn", bound=Callable[..., Incomplete])  # noqa: Y001 # Exists at runtime
__all__ = ("parse_configuration", "read_configuration")

read_configuration = setupcfg.read_configuration
parse_configuration = setupcfg.parse_configuration
