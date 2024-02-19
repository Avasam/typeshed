from abc import abstractmethod
from typing import Any, ClassVar, Literal

from .. import Command

__all__ = ["config_file", "edit_config", "option_base", "setopt"]

def config_file(kind: Literal["local", "global", "user"] = "local"): ...
def edit_config(filename, settings, dry_run: bool = False) -> None: ...

class option_base(Command):
    user_options: ClassVar[list[tuple[str, str, str]]]
    boolean_options: ClassVar[list[str]]
    global_config: Any
    user_config: Any
    filename: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    @abstractmethod
    def run(self) -> None: ...

class setopt(option_base):
    description: ClassVar[str]
    user_options: ClassVar[list[tuple[str, str, str]]]
    boolean_options: ClassVar[list[str]]
    command: Any
    option: Any
    set_value: Any
    remove: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
