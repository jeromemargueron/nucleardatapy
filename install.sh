#/bin/sh

# version number
VER=1.0

# Folder where libraries are installed:
LIB=$HOME/mylib

# Folder where the samples are stored:
# By default, it can be $LIB, but it is not necessary.
#SAMPLES=$LIB

echo ""
echo ">> -----------------------------------"
echo ">> Home path: $HOME"
echo ">> Version: $VER"
echo ">> Folder with toolkit: $LIB"
echo ">> -----------------------------------"
echo ""

echo ">> copy nucleardatapy toolkit to $LIB folder"
cp -R nucleardatapy $LIB

echo ""
echo ">> You should create the following global variables:"
#It will create this environment variable at the compilation
echo ">> export NSEOSFTPY_SO=$HOME/mylib/libnseosft.so"
echo ">> export NSEOSFTPY_TK=$HOME/mylib/nseosftpy"
#echo "env. variable: $NSEOSPY_SO"
# If you do not want to compile each time you log, just copy this last command in your .profile, or .zprofile, or .bashrc, or .bashrc_profile.

# Examples of the two additional environment variable to make the python toolkit working
#export NSEOSPY_PATH=/Users/margueron/ownCloud/GitLab/pydmeos/dev/nseospy/
#export NSEOSPYEXT_PATH=/Users/margueron/ownCloud/GitLab/pydmeos/dev/nseospyext/

