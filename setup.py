# Author: super-string <sh5937tech@gmail.com>
# Copyright (c) 2023- super-string
# License: MIT

from setuptools import setup, find_packages
import pylinqext

NAME = "pylinqext"
DESCRIPTION = "for C#er, you can write code like LINQ."
AUTHOR = "super-string"
AUTHOR_EMAIL = "sh5937tech@gmail.com"
URL = "https://github.com/super-string"
LLICENSE = "MIT"
DOWNLOAD_URL = "https://github.com/super-string"
VERSION = pylinqext.__version__
INSTALL_REQUIRES = None

with open("README.md", "r", encoding="utf_8") as fp:
    readme = fp.read()

long_description = readme

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LLICENSE,
    download_url=DOWNLOAD_URL,
    packages=find_packages()
)