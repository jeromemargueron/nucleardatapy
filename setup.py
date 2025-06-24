from setuptools.command.install import install
import os
from setuptools import setup, find_packages


class CustomInstall(install):
    def run(self):
        os.system("sphinx-build -b html docs docs/_build/html")
        install.run(self)  # Ensure normal install process runs


setup(
    name="nucleardatapy",
    version="1.0.0",
    description="A toolkit for nuclear data processing",
    authors=[
        "Jerome Margueron <marguero@frib.msu.edu>",
        "Sudhanva Lalit <lalit@frib.msu.edu>",
        "Mariana Dutra",
        "Guilherme Grams",
        "Rohit Kumar",
    ],
    package_dir={"": "version-1.0"},
    packages=find_packages(where="version-1.0"),
    include_package_data=True,
    package_data={"nucleardatapy": ["data/*"]},
    install_requires=["numpy", "scipy", "matplotlib", "pandas", "sphinx"],
    # scripts=["install.sh"],
    cmdclass={"install": CustomInstall},
)
