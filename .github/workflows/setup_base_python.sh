#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo
    echo "Please pass GitHub action runner OS (e.g., Linux or macOS)"
    echo
    exit 1
fi
runner_os=$1

which python
which pip
echo " "
python -c "import platform ; print(platform.machine())"
python -c "import platform ; print(platform.system())"
python -c "import platform ; print(platform.release())"
python -c "import platform ; print(platform.platform())"
python -c "import platform ; print(platform.version())"
if [ "$runner_os" = "macOS" ]; then
    python -c "import platform ; print(platform.mac_ver())"
fi
echo " "
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install build
python -m pip install tox
echo " "
python --version
tox --version
echo " "
pip list
echo " "