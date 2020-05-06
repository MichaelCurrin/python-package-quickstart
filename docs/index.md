## Documentation


## Purpose

This project is a quick reference and a demo for making a Python project installable using the `pip install PACKAGE` command. For full details, see the linked resources.


## Resources

- [Packaging Python Projects¶](https://packaging.python.org/tutorials/packaging-projects/) tutorial on [packaging.python.org](https://packaging.python.org).
- [Modules](https://docs.python.org/3/tutorial/modules.html#packages) tutorial in the Python 3 docs.
- [setuptools](https://packaging.python.org/key_projects/#setuptools)
- [wheel](https://packaging.python.org/key_projects/#wheel)


## Guide

### Typical structure

```
packaging_tutorial/
  example_pkg/
    __init__.py
  tests/
  setup.py
  LICENSE
  README.md
```


### The setup.py file


Sample from the tutorial:

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```


### Init

See [section](https://docs.python.org/3/tutorial/modules.html#packages) of tutorial.


What is an `__init__.py` file for?

> The `__init__.py` files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path.
>
> In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable, described later.


### Intra-package references

See [section](https://docs.python.org/3/tutorial/modules.html#intra-package-references) of tutorial.

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Does not work in the main module.
