from _typeshed import Incomplete
from typing_extensions import Final

# These are set by SetupEnvironment when the module is loaded if not frozen (mostly registry values)
__gen_path__: Final[str]
__build_path__: Final[str | None]

def SetupEnvironment() -> None: ...
def __PackageSupportBuildPath__(package_path) -> None: ...

gen_py: Incomplete
