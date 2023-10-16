from typing import Any
from typing_extensions import TypeAlias

JsonType: TypeAlias = str | int | float | bool | None | dict[str, Any] | list[Any]
