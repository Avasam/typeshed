"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Add a dummy package name. Having no package like
core/lib/core/error_codes.proto, or having tensorflow like
tsl/protobuf/error_codes.proto, results in name collision errors in generated
code for some users that use JS through J2CL.
"""

import google.protobuf.descriptor
from tsl.protobuf.status_pb2 import StatusProto as StatusProto

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
