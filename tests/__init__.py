# -*- coding: utf-8 -*-
#
# Copyright (c) 2009 by 2degrees, Ltd. <http://dev.2degreesnetwork.com/>.
# Copyright (c) 2006 by Alexandre Norman <norman@xael.org>.
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
"""
Test suite for Pyclamdplus.

"""

from os import path

from nose.tools import eq_


_here = path.abspath(path.dirname(__file__))
VIRUS_FOLDER = path.join(_here, "fixtures", "viruses")

