# Stubs for networkx.exception (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

class NetworkXException(Exception): ...
class NetworkXError(NetworkXException): ...
class NetworkXPointlessConcept(NetworkXException): ...
class NetworkXAlgorithmError(NetworkXException): ...
class NetworkXUnfeasible(NetworkXAlgorithmError): ...
class NetworkXNoPath(NetworkXUnfeasible): ...
class NetworkXNoCycle(NetworkXUnfeasible): ...
class HasACycle(NetworkXException): ...
class NetworkXUnbounded(NetworkXAlgorithmError): ...
class NetworkXNotImplemented(NetworkXException): ...
class NodeNotFound(NetworkXException): ...
class AmbiguousSolution(NetworkXException): ...
class ExceededMaxIterations(NetworkXException): ...

class PowerIterationFailedConvergence(ExceededMaxIterations):
    def __init__(self, num_iterations, *args, **kw) -> None: ...
