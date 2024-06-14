#/bin/sh

# version number
VER=0.1

# Folder where libraries are installed:
LIB=$HOME/mylib

# Folder where the samples are stored:
# By default, it can be $LIB, but it is not necessary.
SAMPLES=$LIB

echo ""
echo ">> -----------------------------------"
echo ">> Instalation of nucleardatapy toolkit"
echo ">> Home path: $HOME"
echo ">> Version: $VER"
echo ">> Folder with toolkit: $LIB"
echo ">> Folder with samples: $SAMPLES"
echo ">> -----------------------------------"
echo ""
echo ""
echo ">> create a symbolic link to the current version"
rm nucleardatapy
ln -s nucleardatapy-v$VER nucleardatapy

echo ""
echo ">> copy nucleardatapy toolkit to $LIB folder"
cp -R ../nucleardatapy $LIB

echo ""
echo ">> copy nucleardatapy samples to $SAMPLES/samples/ folder"
cp -R samples/nucleardatapy_samples $SAMPLES/samples/

echo ""
echo ">> copy nucleardatapy plots to $SAMPLES/samples folder"
cp -R samples/nucleardatapy_plots $SAMPLES/samples/


echo ""
echo ">> You should create the following global variables:"
echo ">> export NUCLEARDATAPY_TK=$HOME/mylib/nucleardatapy"
echo ""
echo ">> To make you life simpler, just copy this last command to one of the following file in your home: .profile, .zprofile, .bashrc, .bashrc_profile."


