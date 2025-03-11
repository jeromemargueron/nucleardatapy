#/bin/sh

# version number
VER=0.2

# Folder where libraries are installed:
LIB=$HOME/mylib

# Folder where the samples are stored:
# By default, it can be $LIB, but it is not necessary.
SAMPLES=$LIB/nucleardatapy_samples

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
#rm nucleardatapy
#ln -s nucleardatapy-v$VER nucleardatapy

echo ""
echo ">> copy nucleardatapy toolkit to $LIB/nucleardatapy folder"
rm -rf $LIB/nucleardatapy
mkdir -p $LIB/nucleardatapy
mkdir -p $LIB/nucleardatapy/nucleardatapy
cp -R version-$VER/nucleardatapy/* $LIB/nucleardatapy/nucleardatapy
cp -R version-$VER/data $LIB/nucleardatapy/

echo ""
echo ">> copy nucleardatapy samples to $SAMPLES/ folder"
mkdir -p  $SAMPLES
cp -R version-$VER/nucleardatapy_samples/ $SAMPLES/

echo ""
echo ">> You should create the following global variables:"
echo ">> export NUCLEARDATAPY_TK=${HOME}/mylib/nucleardatapy"
echo ""
echo ">> You can also add this link to PYTHONPATH:"
echo ">> export PYTHONPATH=\${NUCLEARDATAPY_TK}"
echo ""
echo ">> To make you life simpler, just copy this last commands "
echo ">> to the following file (depending on your OS): "
echo ">> .profile, .zprofile, .bashrc, .bashrc_profile."
echo ""


