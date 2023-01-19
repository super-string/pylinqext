from setuptools import setup, find_packages

import pylinq

setup(
    name="pylinq",
    version=pylinq.__version__,
    description="for C#er, you can use LINQ like C#",
    author="super-string",
    author_email="sh5937tech@gmail.com",
    url="https://github.com/super-string",
    license="MIT",
    packages=find_packages()
)