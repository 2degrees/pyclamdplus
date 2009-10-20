# -*- coding: utf-8 -*-
#
# Copyright (c) 2009 by 2degrees, Ltd. <http://www.2degreesnetwork.com/>.
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
Exceptions raised by :mod:`pyclamdplus`.

"""

__all__ = ("PyclamdplusException", "ConnectionError", "RequestError",
           "BadTargetError")


class PyclamdplusException(Exception):
    """
    Base exception for Pyclamdplus.
    
    """
    pass


class ConnectionError(PyclamdplusException):
    """
    Exception raised when there was a problem trying to connect to the daemon.
    
    """
    pass


class RequestError(PyclamdplusException):
    """
    Exception raised when Clamd did not execute a request we've made.
    
    """
    pass


class BadTargetError(RequestError):
    """
    Exception raised when a bad target (file or directory) was requested to be
    scanned.
    
    """
    pass

