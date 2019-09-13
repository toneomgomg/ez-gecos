# Copyright (C) 2019 Thomas Hellström <rel@xed.se>
#
# This file is part of ez-gecos.
#
# ez-gecos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ez-gecos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ez-gecos.  If not, see <http://www.gnu.org/licenses/>.

import os.path
from setuptools import setup, find_packages

setup(
    name="ez-gecos",
    version='0.0.0',
    description="Tiny python package to parse the GECOS field.",
    long_description=os.path.join(
        os.path.dirname(__file__),
        "README.md"
    ).read_text(),
    long_description_content_type="text/markdown",
    author="Thomas Hellström",
    author_email="rel@xed.se",
    url="https://github.com/thohell/ez-gecos",
    license='GPLv3',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    # classifiers=[
    #     "License :: OSI Approved :: MIT License",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.7",
    # ],
)
