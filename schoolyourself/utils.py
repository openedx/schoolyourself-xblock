"""Utility file to contain various functions be to used across multiple files."""

from __future__ import absolute_import

from six import text_type


def convert_to_bytes(value):
    """
    Utility method to convert & return type str to type bytes,
    otherwise return the original value.
    """
    if isinstance(value, text_type):
        return value.encode('utf-8')
    return value
