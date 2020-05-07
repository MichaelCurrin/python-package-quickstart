# Online Documentation


## About

This project is a quick reference and a demo for making a Python project installable using the `pip install PACKAGE` command. For full details, see the linked resources.


- _Python 3.6+_
- _Project settings configured for VS Code_


## Resources

### Official docs

Python Packaging site

- [packaging.python.org](https://packaging.python.org) Homepage
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) tutorial. Most of this guide is based on that.
- [Installing packages](https://packaging.python.org/tutorials/installing-packages/) tutorial.
- Key projects
    - [twine](https://packaging.python.org/key_projects/#twine) package - for upload to PyPI.
    - [setuptools](https://packaging.python.org/key_projects/#setuptools) package.
    - [wheel](https://packaging.python.org/key_projects/#wheel) package.

Python 3 docs

- [Modules](https://docs.python.org/3/tutorial/modules.html#packages) tutorial.

### Other

- [How to Publish Your Own Python Package to PyPI](https://realpython.com/courses/how-to-publish-your-own-python-package-pypi/)


## Related projects

- [MichaelCurrin/py-project-template](https://github.com/MichaelCurrin/py-project-template)


## Guide


## What you'll get at the end of this tutorial

- A standard well-structured Python project outline.
- Your project can be installed using `pip` or `python setup.py`.
- Make your project installable using `pip` and a Github URL. 


Note on publishing: 

- This does not cover publishing to PyPI, as that is more restrictive especially if you're a beginner for packaging. For PyPI, you have to setup an account, meet the quality standards (maybe get approval?) and your package becomes searchable. 
- A Github package is lower profile and has lower barriers to experiment with. Also, you can make your project private for your user or org, but still install it where you have access.


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

Note that a directory and a script are both considered a "module" in Python, if it can be imported.

A main file is a script or an entrypoint to be run directly, but it might be considered a module if you import it from elsewhere.


### Init file

See [init file](init_file.md) tutorial page.


### Main file

See [main file](main_file.md) tutorial page.


### Intra-package references

See [section](https://docs.python.org/3/tutorial/modules.html#intra-package-references) of tutorial.

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Does not work in the main module.
