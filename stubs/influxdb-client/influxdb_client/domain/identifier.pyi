from _typeshed import Incomplete

from influxdb_client.domain.property_key import PropertyKey

class Identifier(PropertyKey):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = ..., name: Incomplete | None = ...) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
