#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

from boilerplate import __version__

setuptools.setup(
    name="boilerplate",
    version=__version__,
    description="Python boilerplate project",
    url="https://github.com/westphahl/boilerplate",
    author="Luis Fernando Gomes",
    author_email="luiscoms@ateliedocodigo.com.br",
    license="MIT",
    classifiers=[  # See: https://pypi.python.org/pypi?%3Aaction=list_classifier
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="example boilerplate",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "boilerplate_script = boilerplate.script:main"
        ]
    }
)
