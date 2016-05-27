"""
This is a really simple data persistence module.

It works by unpickling and pickling normal Python data structures.
"""

import os
import os.path
import pickle
import fcntl
import uuid
import re
from bottle import app

def lock_file(fd):
    fcntl.lockf(fd, fcntl.LOCK_EX)

def unlock_file(fd):
    fcntl.lockf(fd, fcntl.LOCK_UN)

def make_uuid():
    return str(uuid.uuid4())


def uuid_filter(config):
    "Matches hexadecimal formatted 16 byte UUID"
    regexp = r"[0-9a-f]{8}(-[0-9a-f]{4}){4}[0-9a-f]{8}"

    def to_python(match):
        return match.group(0)

    def to_url(uuid):
        return str(uuid)

    return regexp, to_python, to_url

# app.router.add_filter('uuid', db.uuid_filter)
