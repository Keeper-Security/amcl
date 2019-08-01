#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck > /dev/null && shellcheck "$0"

# NODEJS_VERSION="8"

LNG=js

# Create the destination directory
DEST=$PWD/dist/$LNG/amcl
mkdir -p ${DEST}

KS_DIR=$PWD/keeper/$LNG

echo "Removing old files in ${DEST}"
rm ${DEST}/* >/dev/null

(
cd version3/$LNG

# These are the files needed for Keeper's library based on BLS12-381
AMCL_FILES="aes.js big.js bls.js bls256.js ctx.js ecdh.js ecp.js ecp2.js fp.js fp12.js fp2.js fp4.js gcm.js hash256.js hash384.js hash512.js mpin.js mpin256.js nhs.js pair.js pair256.js rand.js rom_curve.js rom_field.js sha3.js uint64.js"

KS_FILES="ctx.d.ts package.json"

# Copy the files we need
for f in ${AMCL_FILES}
do
    cp $f ${DEST}/
done

# Copy the files we need
for f in ${KS_FILES}
do
    cp ${KS_DIR}/$f ${DEST}/
done
)

echo "Done collecting JavaScript files for AMCL in ${DEST}"

echo "ls -l ${DEST}: "
ls -l ${DEST}
