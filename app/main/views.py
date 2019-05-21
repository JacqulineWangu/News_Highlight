from . import main
from flask import render_template,url_for,redirect,request
from ..requests import get_sources, get_articles, get_source_news, search_key

@main.route('/')
def index():
    source = get_sources()
    search = request.args.get('news_query')
    if search:
        query = '+'.join( search.split(' ') )

        return redirect( url_for('main.search', words = query ) )
    else:
        return render_template('index.html', sources = source)

@main.route('/sources/<id>')
def headlines(id):

    articles = get_source_news(id)
    search = request.args.get('news_query')
    if search:
        query = '+'.join( search.split(' ') )
        return redirect( url_for('main.search', words = query ) )
    else:    
        return render_template('sources.html', article_data = articles)

@main.route('/search/<words>')
def search(words):
    search_results = search_key(words)
    search = request.args.get('news_query')
    if search:
        query = '+'.join( search.split(' ') )
        return redirect( url_for('main.search', words = query ) )
    else: 
        return render_template('search.html', article_data = search_results)