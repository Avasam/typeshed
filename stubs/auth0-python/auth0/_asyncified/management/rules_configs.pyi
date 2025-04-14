# AUTOGENERATED BY scripts/sync_auth0_python.py
from typing import Any, type_check_only

from auth0.management.rules_configs import RulesConfigs

@type_check_only
class _RulesConfigsAsync(RulesConfigs):
    async def all_async(self) -> list[dict[str, Any]]: ...
    async def unset_async(self, key: str) -> Any: ...
    async def set_async(self, key: str, value: str) -> dict[str, Any]: ...
