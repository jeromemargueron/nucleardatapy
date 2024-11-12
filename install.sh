#/bin/sh

# version number
VER=1.0

# Folder where libraries are installed:
LIB=$HOME/mylib

# Folder where the samples are stored:
# By default, it can be $LIB, but it is not necessary.
SAMPLES=$LIB/nucleardatapy

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
cp -R version$VER/nucleardatapy/* $LIB/nucleardatapy/nucleardatapy
cp -R version$VER/data $LIB/nucleardatapy/

echo ""
echo ">> copy nucleardatapy samples to $SAMPLES/samples/ folder"
mkdir -p  $SAMPLES/samples
cp -R version$VER/samples/nucleardatapy_samples $SAMPLES/samples/

echo ""
echo ">> copy nucleardatapy plots to $SAMPLES/samples folder"
cp -R version$VER/samples/nucleardatapy_plots $SAMPLES/samples/

echo ""
echo ">> You should create the following global variables:"
echo ">> export NUCLEARDATAPY_TK=$HOME/mylib/nucleardatapy"
echo ""
echo ">> To make you life simpler, just copy this last command to one of the following file in your home (depending on your OS): .profile, .zprofile, .bashrc, .bashrc_profile."
echo ""


