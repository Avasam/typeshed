from typing import Any, ClassVar

from .setopt import option_base

def shquote(arg): ...

class alias(option_base):
    description: ClassVar[str]
    command_consumes_arguments: ClassVar[bool]
    user_options: ClassVar[list[tuple[str, str, str]]]
    boolean_options: ClassVar[list[str]]
    args: Any
    remove: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

def format_alias(name, aliases): ...
