from _typeshed import Incomplete

class Suggestion:
    string: Incomplete
    payload: Incomplete
    score: Incomplete
    def __init__(self, string: str, score: float = ..., payload: str | None = ...) -> None: ...

class SuggestionParser:
    with_scores: Incomplete
    with_payloads: Incomplete
    sugsize: int
    def __init__(self, with_scores: bool, with_payloads: bool, ret) -> None: ...
    def __iter__(self): ...
