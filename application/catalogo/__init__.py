from flask import Blueprint

catalogo = Blueprint('catalogo', __name__, template_folder='templates')

from . import routes