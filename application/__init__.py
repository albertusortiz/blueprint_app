from flask import Flask
from .inicio import inicio
from .catalogo import catalogo
from .contacto import contacto

app = Flask(__name__)

app.config.from_pyfile('config/configuration.cfg')

app.register_blueprint(inicio)
app.register_blueprint(catalogo)
app.register_blueprint(contacto)
