# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

import os.path
import sys

# add your project directory to the sys.path
project_home = os.path.expanduser("~/guestbook")
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

import bottle

# make sure the default templates directory is known to Bottle
templates_dir = os.path.join(project_home, 'views/')
if templates_dir not in bottle.TEMPLATE_PATH:
    bottle.TEMPLATE_PATH.insert(0, templates_dir)

# import your application
from app import application
