# AUTOGENERATED BY scripts/sync_auth0_python.py
from typing import Any, type_check_only

from auth0.management.users_by_email import UsersByEmail

@type_check_only
class _UsersByEmailAsync(UsersByEmail):
    async def search_users_by_email_async(
        self, email: str, fields: list[str] | None = None, include_fields: bool = True
    ) -> list[dict[str, Any]]: ...
