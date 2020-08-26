# Installation


## Install system dependencies

Install Python 3.6 or higher.

## Setup virtual environment

Create a virtual environment.

Activate it.


## Install from project

This requires this project to be cloned or downloaded.

Install the project:

```sh
$ python setup.py sdist bdist_wheel
```

<!-- 

TBC if these from SoloLearn are still accurate as is differs from the above.

Build a source distribution:

```sh
$ python setup.py sdist
```

Build a binary distribution:

```sh
$ python setup.py bdist
# Windows
> python setup.py bdist_wininst
```

-->


## Install from packages repository

- [PyPI](https://pypi.org/) (for a published package).
    ```python
    $ pip install PACKAGE_NAME
    ```
- GitHub:
    ```sh
    $ pip install -e git+https://github.com/MichaelCurrin/python-package-quickstart.git@master
    ```

Change the reference at the end with a commit reference like a commit hash, branch name or tag.

### Egg

Based on [blog post](https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/).

Include dependencies.

- Git repo
    ```sh
    $ pip install -e git+https://github.com/django/django.git@45dfb3641aa4d9828a7c5448d11aa67c7cbd7966#egg=django[argon2]
    ```
- Tarball
    ```sh
    $ pip install -e https://github.com/django/django/archive/45dfb3641aa4d9828a7c5448d11aa67c7cbd7966.tar.gz#egg=django[argon2]
    ```

> Any URL may use the #egg=name syntax (see VCS Support) to explicitly state the project name. [source](https://pip.pypa.io/en/stable/reference/pip_install/)

```
[-e] git+https://git.example.com/MyProject#egg=MyProject
```

## Install from zipped archive

Download a tarball file.

```sh
$ pip install master.tar.gz
```

Install from the repo:

e.g.

- GitHub
    ```sh
    $ pip install https://github.com/django/django/archive/master.tar.gz
    ```
- GitLab
    ```sh
    $ pip install https://gitlab.com/pycqa/flake8/-/archive/3.7.7/flake8-3.7.7.tar.gz
    ```
- Bitbucket
    ```sh
    $ pip install https://bitbucket.org/hpk42/tox/get/2.3.1.tar.gz
    ```
