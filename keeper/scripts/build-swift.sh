#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck > /dev/null && shellcheck "$0"

LNG=swift

# Create the destination directory
DEST=$PWD/dist/$LNG/amcl
mkdir -p ${DEST}

KS_DIR=$PWD/keeper/$LNG

echo "Removing old files in ${DEST}"
rm -rf ${DEST}/* >/dev/null

(
    cd version3/$LNG

    # Remove old target directory
    if [ -d amcl ]
    then
        rm -rf amcl
    fi
    

python3 ${KS_DIR}/config64.py <<END_OF_INPUT
21
0
END_OF_INPUT

# Copy the collected files to DEST
cp -pr amcl/* $DEST/
)

echo ""
echo "Done collecting $LNG files for AMCL in ${DEST}"

echo "ls -l ${DEST}: "
ls -l ${DEST}
