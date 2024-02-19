from collections.abc import Callable
from typing import Any, ClassVar
from typing_extensions import Self

from .._distutils.command import install as orig

class install(orig.install):
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    boolean_options: ClassVar[list[str]]
    new_commands: ClassVar[list[tuple[str, Callable[[Self], bool]]]]
    old_and_unmanageable: Any
    single_version_externally_managed: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    path_file: Any
    extra_dirs: str
    def handle_extra_path(self): ...
    def run(self): ...
    def do_egg_install(self) -> None: ...
