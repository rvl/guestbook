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
from collections import OrderedDict
import datetime
from bottle import app

storage = {}

def load_file(name):
    try:
        with open(db_path(name), "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        pass
    except OSError as e:
        print("Error opening database %s: %s" % (name, e))
    return None

def save_file(name, data):
    try:
        os.makedirs(db_dir, exist_ok=True)
        with open(db_path(name), "wb") as f:
            pickle.dump(data, f)
    except OSError as e:
        print("Error saving database %s: %s" % (name, e))

db_dir = os.path.join(os.path.dirname(__file__), "_db")

def db_path(name):
    return os.path.join(db_dir, name)

def get_collection(name):
    global storage
    if name not in storage:
        storage[name] = load_file(name) or OrderedDict()
    return storage[name]

def put_collection(name, data):
    global storage
    storage[name] = data
    save_file(name, data)

def collection_insert(name, item):
    col = get_collection(name)
    item["id"] = make_uuid()
    col[item["id"]] = item
    put_collection(name, col)
    return item

def timestamp():
    return datetime.datetime.now().isoformat()

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
