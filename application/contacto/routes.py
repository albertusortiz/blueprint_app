from flask import render_template
from . import contacto

@contacto.route('/contacto', methods=['GET'])
def contacto():
    return render_template('contacto.html')