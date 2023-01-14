from typing import Any

from .context import SpanContext

class Propagator:
    def inject(self, span_context: SpanContext, carrier: dict) -> None: ...
    def extract(self, carrier: dict) -> SpanContext: ...
