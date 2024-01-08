from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in datavalue_theme_14/__init__.py
from datavalue_theme_14 import __version__ as version

setup(
	name="datavalue_theme_14",
	version=version,
	description="Data Value 14 Theme",
	author="Abdo Hamoud",
	author_email="abdo.host@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
