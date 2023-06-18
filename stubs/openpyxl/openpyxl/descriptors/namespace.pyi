from _typeshed import Unused
from typing import overload

@overload
def namespaced(obj, tagname: Unused, namespace: str) -> str: ...
@overload
def namespaced(obj, tagname: str, namespace: None = None) -> str: ...
