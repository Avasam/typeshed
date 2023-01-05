from typing import Any

from passlib.context import LazyCryptContext

linux_context: Any
linux2_context: Any
freebsd_context: Any
openbsd_context: Any
netbsd_context: Any
# Only exists if crypt is installed
host_context: LazyCryptContext
