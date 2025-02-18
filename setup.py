from setuptools.command.install import install
import os
from setuptools import setup, find_packages


class CustomInstall(install):
    def run(self):
        os.system("sphinx-build -b html docs docs/_build/html")
        os.system("sphinx-build -b html docs docs/_build/html")


setup(
    name="nucleardatapy",
    version="1.0",
    description="A toolkit for nuclear data processing",
    author="Nuclear Data Group",
    author_email="",
    package_dir={"": "version1.0"},
    packages=find_packages(where="version1.0"),
    install_requires=["numpy", "scipy", "matplotlib", "pandas", "sphinx"],
    scripts=["install.sh"],
    cmdclass={"install": CustomInstall},
)
