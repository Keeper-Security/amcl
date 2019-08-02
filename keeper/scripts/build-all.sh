#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck > /dev/null && shellcheck "$0"

# Build all of the Pythia libraries

echo "Building Java"
(
bash scripts/build-java.sh
)

echo "Building JavaScript"
(
bash scripts/build-js.sh
)

echo "Building Swift"
(
bash scripts/build-swift.sh
)
