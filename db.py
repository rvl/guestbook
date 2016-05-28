"""
This is a highly unsophisticated data persistence module.

It works by unpickling and pickling normal Python data structures.

For large amounts of data or multi-threaded servers, you will need to
use something better, like sqlite.
"""

import datetime
import os
import os.path
import pickle
import re
import uuid
from bottle import app
from collections import OrderedDict

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

def make_uuid():
    return str(uuid.uuid4())
