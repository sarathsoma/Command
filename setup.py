# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='fecho',
    version="1.0",
    packages=find_packages(),
    pymodules=["fecho"],
    include_package_data=False,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        fecho=fecho.command:fecho
    """
)
