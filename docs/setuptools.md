# Setuptools


## Setup file


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

Notes:

- Some metadata fields like `"long_description_content_type"` will only work on newer versions `setuptools>=38.6.0` - see [issue](https://github.com/di/markdown-description-example/issues/4). Update `sdist` as well, to avoid warnings.
- There's a warning that if author name is setup, then author email must be set too.


## Install and upgrade system dependencies

Make sure you have the latest version of `setuptools` installed at the user level for Python 3. i.e. Run this _outside_ a virtual environment and with the `--user` flag.

From the tutorial:

```sh
python3 -m pip install --user --upgrade setuptools wheel
```

If you don't use the `--user` flag, you might get errors on install for Python managed by root and then have to use `sudo`, which should be avoided in general when installing Python packages.

Those are stored in site packages.

e.g. `.local/lib/python3.5/site-packages` on Linux.


Follow [Installation](installation.md) page for installing the project package.
