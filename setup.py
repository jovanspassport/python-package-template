"""Setup for this package."""

import ast
import os
import typing

import setuptools

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as fh:
    README = fh.read()
with open(os.path.join(here, "LICENSE.md")) as fh:
    LICENSE = fh.read()
with open(os.path.join(here, "package", "__init__.py")) as fh:
    module = ast.parse(next(filter(lambda line: line.startswith("__version__"), fh)))
    assign = typing.cast(ast.Assign, module.body[0])
    # See also: https://github.com/relekang/python-semantic-release/issues/388
    VERSION = typing.cast(ast.Constant, assign.value).s

# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
# https://docs.python.org/3/distutils/apiref.html#distutils.core.setup
setuptools.setup(
    name="package",
    version=VERSION,
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    # maintainer=
    # maintainer_email=
    license=LICENSE,
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="",
    project_urls={
        "Homepage": "https://foo.bar/",
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    include_package_data=True,
    install_requires=[],
    extras_require={
        "test": ["hypothesis==6.21.6", "pytest==6.2.4", "pytest-cov==2.12.1"],
        "dev": [
            "flake8==3.9.2",
            "flake8-builtins==1.5.3",
            "flake8-docstrings==1.6.0",
            "flake8-rst-docstrings==0.2.3",
            "mypy==0.910",
            "pep8-naming==0.12.1",
            "pre-commit==2.13.0",
            "pylint==2.9.3",
            "python-semantic-release==7.16.2",
        ],
        "docs": ["sphinx==4.1.2"],
    },
    package_data={},
    options={},
    platforms="",
    zip_safe=False,
)