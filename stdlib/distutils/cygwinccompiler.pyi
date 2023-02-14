from _typeshed import Incomplete
from distutils.unixccompiler import UnixCCompiler
from distutils.version import LooseVersion
from typing_extensions import Literal

def get_msvcr() -> list[str] | None: ...

class CygwinCCompiler(UnixCCompiler): ...
class Mingw32CCompiler(CygwinCCompiler): ...

CONFIG_H_OK: str
CONFIG_H_NOTOK: str
CONFIG_H_UNCERTAIN: str

def check_config_h() -> tuple[Literal["ok", "not ok", "uncertain"], str]: ...

RE_VERSION: Incomplete

def get_versions() -> tuple[LooseVersion | None, ...]: ...
def is_cygwingcc() -> bool: ...
