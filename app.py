#!/usr/bin/env python3

from bottle import route, run, template, static_file, abort, request
import os.path
import db

############################################################################
# Simple pages

@route('/')
def home():
    return template("home")

@route('/about')
def about():
    return template("about")

############################################################################
# Dynamic pages

@route('/write')
def message_create():
    if request.method == "POST":
        msg = {
        }
    else:
        msg = {
            "title": "",
            "text": "",
            "author": "",
        }

    return template("message_edit", message=msg)

@route('/messages')
def message_list():
    msgs = db.get_collection("msg")
    return template("message_list", messages=msgs)

@route('/messages/<id>')
def message_detail(id=None):
    msgs = db.get_collection("msg")
    msg = msgs.get(id)
    if msg:
        return template("message_detail", message=msg)
    else:
        abort(404, "Message not found")

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=os.path.join(os.path.dirname(__file__), "static"))

run(host='localhost', port=8080, debug=True)
