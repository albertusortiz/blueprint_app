from flask import Blueprint

contacto = Blueprint('contacto', __name__, template_folder='templates')

from . import routes



