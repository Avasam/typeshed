from typing import ClassVar

from .setopt import option_base

class saveopts(option_base):
    description: ClassVar[str]
    def run(self) -> None: ...
