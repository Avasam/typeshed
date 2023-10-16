from redis.typing import EncodableT

from ..exceptions import DataError as DataError

class Encoder:
    encoding: str
    encoding_errors: str
    decode_responses: bool
    def __init__(self, encoding: str, encoding_errors: str, decode_responses: bool) -> None: ...
    def encode(self, value: EncodableT) -> bytes: ...
    def decode(self, value: str | bytes | memoryview, force: bool = False) -> str: ...
