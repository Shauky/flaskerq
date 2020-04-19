#Register main app here
from flask import Blueprint
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__)

from . import views
