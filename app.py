#!/usr/bin/env python

import os
from bottle import route, run, static_file, template, view

# Main Static Passing Calls

@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')

@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./img')

@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./css')

@route('/fancybox/<filename>')
def img_static(filename):
    return static_file(filename, root='./fancybox')

@route('/font/<filename>')
def img_static(filename):
    return static_file(filename, root='./font')

@route('/images/<filename>')
def img_static(filename):
    return static_file(filename, root='./images')

@route('/images/portfolio/<filename>')
def img_static(filename):
    return static_file(filename, root='./images/portfolio')


# Additional Static Call
@route('/static/:filename:')
def send_static(filename):
    return static_file(filename, root='./static/')

# Static Routing

@route("/")
@view("main")
def hello():
    return dict(title = "MetaSim Platform", content = "Introducting the MetaSim Platform project! Distributed multi-disciplinary simulation!")

# Call index.html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7008))
    run(host='0.0.0.0', port=port)
