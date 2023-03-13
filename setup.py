#!/usr/bin/env python
# coding: utf-8
import re

from setuptools import setup


def get_version():
    VERSIONFILE = "geoconvert/__init__.py"
    initfile_lines = open(VERSIONFILE, "rt").readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
    name="Geoconvert",
    author="OctopusMind",
    author_email="informatique@octopusmind.info",
    version=get_version(),
    license="MIT",
    packages=["geoconvert", "geoconvert/data", "geoconvert/data/subdivisions"],
)
