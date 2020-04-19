from flask import render_template, flash, redirect, url_for, request, \
    current_app, abort, make_response, jsonify
from jinja2 import Environment, PackageLoader, select_autoescape
from . import main

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
# For base authentication
@main.route('/auth/<string:page_name>/')
def render_static(page_name):
    template = env.get_template('%s.html' % page_name)   #templating should be better
    return(template.render())      #</string:page_name>

# For base pages
@main.route('/<string:page_name>/')
def render_errors(page_name):
    template = env.get_template('%s.html' % page_name)
    return(template.render())      #</string:page_name>

#  App Entry
@main.route('/')
def index_view():
    lists = ["tasks", "getdone", "completed", "in progress"]
    template = env.get_template('index.html')
    return(template.render(**locals()))              #renders local values onto page

if __name__ == '__main__':
    main.run()
