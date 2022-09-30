from typing import Any
from typing_extensions import Literal

DATE: str
NUMBER: str
RAW: str
SQL_FETCH_ABSOLUTE: int
SQL_FETCH_FIRST: int
SQL_FETCH_FIRST_SYSTEM: int
SQL_FETCH_FIRST_USER: int
SQL_FETCH_LAST: int
SQL_FETCH_NEXT: int
SQL_FETCH_PRIOR: int
SQL_FETCH_RELATIVE: int
STRING: str
TYPES: tuple[Literal["STRING"], Literal["RAW"], Literal["NUMBER"], Literal["DATE"]]

class dataError(Exception): ...
class error(Exception): ...
class integrityError(Exception): ...
class internalError(Exception): ...
class noError(Exception): ...
class opError(Exception): ...
class progError(Exception): ...

def SQLDataSources(*args, **kwargs) -> Any: ...
def odbc(*args, **kwargs) -> Any: ...
