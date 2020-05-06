"""
Sample project setup file.
"""
import setuptools
from setuptools import setup

with open("README.md") as f_in:
    long_description = f_in.read()


setup(
    name="sample-project-MichaelCurrin",
    version="0.0.1",
    author="Michael Currin",
    author_email="",
    description="A sample Python package project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichaelCurrin/python-package-quickstart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
