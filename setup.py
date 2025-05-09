from setuptools.command.install import install
import os
from setuptools import setup, find_packages


class CustomInstall(install):
    def run(self):
        os.system("sphinx-build -b html docs docs/_build/html")
        install.run(self)  # Ensure normal install process runs


setup(
    name="nucleardatapy",
    version="0.2",
    description="A toolkit for nuclear data processing",
    author="Nuclear Data Group",
    author_email="",
    package_dir={"": "version-0.2"},
    packages=find_packages(where="version-0.2"),
    include_package_data=True,
    package_data={"nucleardatapy": ["data/*"]},
    install_requires=["numpy", "scipy", "matplotlib", "pandas", "sphinx"],
    # scripts=["install.sh"],
    cmdclass={"install": CustomInstall},
)
