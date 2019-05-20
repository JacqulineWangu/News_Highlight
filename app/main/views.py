from . import main
from flask import render_template,url_for,redirect

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/headlines')
def headlines():
    return render_template('/headlines')