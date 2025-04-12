# AUTOGENERATED BY scripts/sync_auth0_python.py
from typing import Any, type_check_only

from auth0.management.branding import Branding

@type_check_only
class _BrandingAsync(Branding):
    async def get_async(self) -> dict[str, Any]: ...
    async def update_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def get_template_universal_login_async(self) -> dict[str, Any]: ...
    async def delete_template_universal_login_async(self) -> Any: ...
    async def update_template_universal_login_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
    async def get_default_branding_theme_async(self) -> dict[str, Any]: ...
    async def get_branding_theme_async(self, theme_id: str) -> dict[str, Any]: ...
    async def delete_branding_theme_async(self, theme_id: str) -> Any: ...
    async def update_branding_theme_async(self, theme_id: str, body: dict[str, Any]) -> dict[str, Any]: ...
    async def create_branding_theme_async(self, body: dict[str, Any]) -> dict[str, Any]: ...
