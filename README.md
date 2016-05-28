# Guestbook Example App

This is a small application which you can use as a model or base for
your own project.

The code is here, which you should browse and download:

  https://github.com/rvl/guestbook

And you can (probably) see it in action here:

  http://rvl.pythonanywhere.com/

![Screenshot](/screenshot.png?raw=true "Screenshot")

Note how it appears on a computer as well as on a phone.


## Getting started

A good editor to use for Python and HTML is
[Sublime Text 3][sublime]. You can download a trial version for free.

To understand how it works examine [`app.py`](./app.py) and skim the
[Bottle tutorial][btut]. You can look through each of the HTML files
in the [`views/`](./views/) directory to see how variables are used in
templates.

To start the development server, either:
1. Run `app.py` from IDLE
2. Open `app.py` in Sublime Text then press <kbd>⌘</kbd>+<kbd>B</kbd>

Then visit http://localhost:8080/ .


## Doing your thing

Try editing stuff in the HTML files, then refresh the page and see
what happens.

Start making simple changes to `app.py`, then stop and restart the
development server. For example, add the "hello world" example view
from the Bottle tutorial. If the development server successfully
starts, refresh the web page to see what changed.

As a rule, you need to restart the development server for Python code
changes to take effect. If it is a HTML change, then you only need to
refresh the web browser.

## Learning more

[Bottle](http://bottlepy.org/) is well documented and there is plenty
of information on the website to get you started.

[Bootstrap 3](http://getbootstrap.com/) makes the app look nice, kind
of like Twitter. Generally, you just browse through the examples on
the web site, pick what looks nice, then copy & paste the HTML code
into your template.

For example, to make a large green button, visit
[CSS / Buttons](http://getbootstrap.com/css/#buttons). Change the
button text as appropriate, maybe add a
[Glyphicon](http://getbootstrap.com/components/#glyphicons)

To make a list group of links, get the code from
[Components / List group](http://getbootstrap.com/components/#list-group-linked),
and fix up the text and `href="#"` attributes.

The HTML code looks like a mess but you get used to it.

## Storage "Database"

The example app uses a really simple data storage system. It is no
more complex than necessary for a small application.

It works by "pickling" and "unpickling" Python objects using the
[pickle module][pickle]. The pickled objects are stored in files in a
`_db/` directory.

The storage code can be edited in [`db.py`](./db.py).

## Other things

There are also javascript and CSS files within the
[`static/`](./static/) directory.

## Setting up hosting on Python Anywhere

[Python Anywhere][pa] is really easy and gives away trial accounts for
small projects.

1. Sign up for [Python Anywhere][pa]
2. From the Dashboard, create a new web app. Use the "Manual setup"
   option.
3. Then create a Bash console and type:
   ```
   git clone https://github.com/rvl/guestbook.git
   ```
4. In the web app configuration section, edit the *WSGI configuration
   file* so that it looks like
   [`wsgi/pythonanywhere.py`](./wsgi/pythonanywhere.py).
5. Click the *Reload* button then try viewing your web site.

## Simulating a Phone in Chrome

It's not always convenient to use a phone for testing.

To simulate a phone inside a desktop web browser, either resize your
window, or use [Device Mode][dm] in Chrome.

[Device Mode][dm] can be activated by pressing
<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>J</kbd> then
<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>.

## Licence

You're free to use this code as you wish: MIT Licence.

[pa]: https://www.pythonanywhere.com/
[sublime]: https://www.sublimetext.com/
[btut]: http://bottlepy.org/docs/dev/tutorial.html
[dm]: https://developers.google.com/web/tools/chrome-devtools/iterate/device-mode/
[pickle]: https://docs.python.org/3/library/pickle.html
