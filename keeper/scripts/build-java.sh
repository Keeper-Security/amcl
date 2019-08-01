#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck > /dev/null && shellcheck "$0"

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
# Delete old version
echo "Removing existing files in dist/java"
rm dist/java/*.jar > /dev/null

echo "Checking for new amcl-3.*.jar"
JAR_FILE=`find . -name 'amcl*.jar'`

echo "Copying ${JAR_FILE} to the dist/java folder"
if [ -f "${JAR_FILE}" ]
then
    cp ${JAR_FILE} dist/java/
fi

echo "ls -l dist/java: "
ls -l dist/java
