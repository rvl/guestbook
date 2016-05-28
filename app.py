#!/usr/bin/env python3

from bottle import route, run, template, static_file, abort, request, default_app
import os.path
import db

############################################################################
# Simple pages

@route("/")
def home():
    return template("home")

@route("/about")
def about():
    return template("about")

############################################################################
# Dynamic pages

@route("/write", method="GET")
def message_create():
    """
    Shows the message editing/creation form.
    """
    msg = {
        "title": "",
        "text": "",
        "author": "",
    }
    return template("message_edit", msg=msg, errors=[])

@route("/write", method="POST")
def do_message_create():
    """
    Receives a new message and saves it into database.
    If successful, shows a confirmation.
    If problem, shows the form with error messages.
    """
    msg = {
        "title": request.forms.get("title"),
        "text": request.forms.get("text"),
        "author": request.forms.get("author"),
        "private": request.forms.get("private") == "checked",
        "time": db.timestamp(),
    }
    errors = []

    if not msg["title"] and not msg["text"]:
        errors.append("Please supply a title or message")

    if not errors:
        msg = db.collection_insert("msg", msg)
        return template("message_success", msg=msg)
    else:
        return template("message_edit", msg=msg, errors=errors)

@route("/messages")
def message_list():
    """
    Shows a list of messages.
    """
    msgs = db.get_collection("msg").values()
    return template("message_list", msgs=msgs)

@route("/messages/<id>")
def message_detail(id=None):
    msgs = db.get_collection("msg")
    msg = msgs.get(id)
    if msg:
        return template("message_detail", msg=msg)
    else:
        abort(404, "Message not found")

@route("/stats")
def stats():
    msgs = db.get_collection("msg")
    stats = {
        "count": len(msgs),
        "num_authors": len(set(msg.get("author") for msg in msgs.values())),
        "longest": max(len(msg.get("text", "")) for msg in msgs.values()),
    }
    return template("stats", **stats)


############################################################################
# Static file serving. Makes files in ./static/ directory accessible
# from web server.

@route("/static/<path:path>")
def static_serve(path):
    return static_file(path, root=os.path.join(os.path.dirname(__file__), "static"))


############################################################################
# Application variable -- used by WSGI web hosting

application = default_app()


############################################################################
# Development server main function.
# Run this python file and you will get a development server available
# at http://localhost:8080/

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
