from . import main
from flask import render_template,url_for,redirect
from ..requests import get_sources

@main.route('/')
def index():
    source = get_sources()
    return render_template('index.html', sources = source)

# @main.route('/headlines')
# def headlines():
#     return render_template('headlines.html')