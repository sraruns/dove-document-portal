from setuptools import setup, find_packages

setup(
    name="document-portal",
    author="Arun Selva",
    version="0.1",
    # Tell setuptools that packages are under the 'src' directory
    package_dir={'': 'src'},
    # Tell find_packages where to start looking for packages
    packages=find_packages(where='src'),
)