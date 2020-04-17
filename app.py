from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# For base pages
@app.route('/<string:page_name>/')
def render_static(page_name):
    template = env.get_template('%s.html' % page_name)
    return(template.render())      #</string:page_name>

#  App Entry
@app.route('/')
def index_view():
    lists = ["tasks", "getdone", "completed", "in progress"]
    template = env.get_template('index.html')
    return(template.render(**locals()))              #renders local values onto page


if __name__ == '__main__':
    app.run()
