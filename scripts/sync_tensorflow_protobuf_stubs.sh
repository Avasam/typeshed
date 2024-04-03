#!/bin/bash
# Partly based on scripts/generate_proto_stubs.sh.
# Generates the protobuf stubs for the given tensorflow version using mypy-protobuf.
# Generally, new minor versions are a good time to update the stubs.
set -euxo pipefail

# Need protoc >= 3.15 for explicit optional
PROTOBUF_VERSION=25.3 # 4.25.3
# Whenever you update TENSORFLOW_VERSION here, version should be updated
# in stubs/tensorflow/METADATA.toml and vice-versa.
TENSORFLOW_VERSION=2.16.1
# Latest mypy-protobuf has dependency on protobuf >4, which is incompatible at runtime
# with tensorflow. However, the stubs produced do still work with tensorflow.
# This issue is mitigated by using a different venv
MYPY_PROTOBUF_VERSION=3.5.0

if uname -a | grep Darwin; then
    # brew install coreutils wget
    PLAT=osx
else
    PLAT=linux
fi
REPO_ROOT="$(realpath "$(dirname "${BASH_SOURCE[0]}")"/..)"
TMP_DIR="$(mktemp -d)"
TENSORFLOW_FILENAME="v$TENSORFLOW_VERSION.zip"
PROTOC_FILENAME="protoc-$PROTOBUF_VERSION-$PLAT-x86_64.zip"
PROTOC_URL="https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOBUF_VERSION/$PROTOC_FILENAME"
TENSORFLOW_URL="https://github.com/tensorflow/tensorflow/archive/refs/tags/$TENSORFLOW_FILENAME"

cd "$TMP_DIR"
echo "Working in $TMP_DIR"

# Install protoc
wget "$PROTOC_URL"
mkdir protoc_install
unzip "$PROTOC_FILENAME" -d protoc_install
protoc_install/bin/protoc --version

# Fetch tensorflow (which contains all the .proto files)
wget "$TENSORFLOW_URL"
unzip "$TENSORFLOW_FILENAME"
TENSORFLOW_DIR="tensorflow-$TENSORFLOW_VERSION"

# Prepare virtualenv
uv venv .venv
source .venv/bin/activate
uv pip install pre-commit mypy-protobuf=="$MYPY_PROTOBUF_VERSION"


# Folders here cover the more commonly used protobufs externally and
# their dependencies. Tensorflow has more protobufs and can be added if requested.
protoc_install/bin/protoc \
    --proto_path="$TENSORFLOW_DIR/third_party/xla/third_party/tsl" \
    --proto_path="$TENSORFLOW_DIR/third_party/xla" \
    --proto_path="$TENSORFLOW_DIR" \
    --mypy_out "relax_strict_optional_primitives:$REPO_ROOT/stubs/tensorflow" \
    $TENSORFLOW_DIR/third_party/xla/xla/*.proto \
    $TENSORFLOW_DIR/third_party/xla/xla/service/*.proto \
    $TENSORFLOW_DIR/tensorflow/core/example/*.proto \
    $TENSORFLOW_DIR/tensorflow/core/framework/*.proto \
    $TENSORFLOW_DIR/tensorflow/core/protobuf/*.proto \
    $TENSORFLOW_DIR/tensorflow/core/protobuf/tpu/*.proto \
    $TENSORFLOW_DIR/tensorflow/core/util/*.proto \
    $TENSORFLOW_DIR/tensorflow/python/keras/protobuf/*.proto \
    $TENSORFLOW_DIR/third_party/xla/third_party/tsl/tsl/protobuf/*.proto

# Cleanup after ourselves, this is a temp dir, but it can still grow fast if run multiple times
rm -rf "$TMP_DIR"

cd "$REPO_ROOT"

# These protos exist in a folder with protos used in python, but are not
# included in the python wheel. They are likely only used for other
# language builds. stubtest was used to identify them by looking for
# ModuleNotFoundError.
rm stubs/tensorflow/xla/service/hlo_execution_profile_data_pb2.pyi \
   stubs/tensorflow/xla/service/hlo_profile_printer_data_pb2.pyi \
   stubs/tensorflow/xla/service/test_compilation_environment_pb2.pyi \
   stubs/tensorflow/xla/xla_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/autotuning_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/conv_autotuning_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/critical_section_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/eager_service_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/master_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/master_service_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/replay_log_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/tpu/compile_metadata_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/worker_pb2.pyi \
   stubs/tensorflow/tensorflow/core/protobuf/worker_service_pb2.pyi \
   stubs/tensorflow/tensorflow/core/util/example_proto_fast_parsing_test_pb2.pyi


sed --in-place="" \
    "s/extra_description = .*$/extra_description = \"Partially generated using [mypy-protobuf==$MYPY_PROTOBUF_VERSION](https:\/\/github.com\/nipunn1313\/mypy-protobuf\/tree\/v$MYPY_PROTOBUF_VERSION) on tensorflow==$TENSORFLOW_VERSION\"/" \
    "$REPO_ROOT/stubs/tensorflow/METADATA.toml"

# Keep pre-commit run after cleanup to reduce changed files. Or start using a temp folder for this script
# use `|| true` so the script still continues even if a pre-commit hook
# applies autofixes (which will result in a nonzero exit code)
pre-commit run --files $(git ls-files -- "$REPO_ROOT/stubs/tensorflow/tensorflow/**.pyi") || true
# Ruff takes two passes to fix everything, re-running all of pre-commit is *slow*
# and we don't need --unsafe-fixes to remove imports
ruff check "$REPO_ROOT/stubs/tensorflow/tensorflow" --fix --exit-zero
