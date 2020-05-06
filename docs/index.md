# Online Documentation


## About

This project is a quick reference and a demo for making a Python project installable using the `pip install PACKAGE` command. For full details, see the linked resources.


- _Python 3.6+_
- _Project settings configured for VS Code_


## Resources

- [packaging.python.org](https://packaging.python.org)
    - [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/) tutorial. Most of this guide is based on that.
    - [Installing packages](https://packaging.python.org/tutorials/installing-packages/) tutorial.
- [Modules](https://docs.python.org/3/tutorial/modules.html#packages) tutorial in the Python 3 docs.
- [setuptools](https://packaging.python.org/key_projects/#setuptools)
- [wheel](https://packaging.python.org/key_projects/#wheel)


## Related projects

- [MichaelCurrin/py-project-template](https://github.com/MichaelCurrin/py-project-template)


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

Note that a directory and a script are both considered a "module" in Python, if it can be imported.

A main file is a script or an entrypoint to be run directly, but it might be considered a module if you import it from elsewhere.


### Init file

See [init file](init_file.md) tutorial page.


### Intra-package references

See [section](https://docs.python.org/3/tutorial/modules.html#intra-package-references) of tutorial.

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

Does not work in the main module.
