#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck > /dev/null && shellcheck "$0"

LNG=java

# Create the destination directory
DEST=$PWD/dist/$LNG/amcl
mkdir -p ${DEST}

echo "Removing old files in ${DEST}"
rm -rf ${DEST}/* >/dev/null

(
cd version3/java

python3 config64.py <<END_OF_INPUT
21
0
END_OF_INPUT

cd amcl
mvn clean install
)

echo "Done building Java version of AMCL."

echo "Checking for new amcl*.jar"
JAR_FILE=`find . -name 'amcl*.jar'`

echo "Copying ${JAR_FILE} to ${DEST}"
if [ -f "${JAR_FILE}" ]
then
cp ${JAR_FILE} ${DEST}/
fi

echo "ls -l ${DEST}: "
ls -l ${DEST}
