from flask import render_template
from . import inicio

@inicio.route('/', methods=['GET'])
@inicio.route('/inicio', methods=['GET'])
def index():
    return render_template('index.html')