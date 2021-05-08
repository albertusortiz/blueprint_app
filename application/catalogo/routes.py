from flask import render_template
from . import catalogo

@catalogo.route('/catalogo', methods=['GET'])
def catalogos():
    return render_template('catalogo.html')