#!/bin/bash -e

cd dist
INSTALLER_VERSION=$(cat version)
echo $INSTALLER_VERSION
sftp -o "StrictHostKeyChecking no" -P 2244 minelabs@minelabs.be<< EOF
cd download/installer
mkdir $INSTALLER_VERSION
cd $INSTALLER_VERSION
put *.exe
cd ..
rm latest
ln -s ./$INSTALLER_VERSION latest
bye
EOF