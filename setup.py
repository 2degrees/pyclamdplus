# -*- coding: utf-8 -*-
#
# Copyright (c) 2009, 2011, 2015 by 2degrees, Ltd.
# <http://dev.2degreesnetwork.com/>.
#
# This file is part of Pyclamdplus.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = open(os.path.join(HERE, "VERSION.txt")).readline().rstrip()
README = open(os.path.join(HERE, "README.rst")).read()

setup(name="pyclamdplus",
      version=VERSION,
      description="Pythonic interface to the Clamav daemon",
      long_description=README,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Security"
        ],
      keywords="clamav clamd pyclamav pyclamd antivirus anti-virus virus",
      author="2degrees Limited",
      author_email="2degrees-floss@googlegroups.com",
      license="GNU GPL v2 or later (http://www.gnu.org/licenses/gpl-2.0.html)",
      packages=find_packages(exclude=["tests"]),
      package_data={
        '': ['VERSION.txt', 'README.rst'],
        },
      zip_safe=False,
      tests_require=["coverage >= 3.0", "nose >= 0.11.0"],
      install_requires=["six"],
      test_suite="nose.collector",
      )

