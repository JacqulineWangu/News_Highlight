import urllib.request, json
from .models import Sources, Articles

api_key = None
search_url = None
news_url = None
articles_url = None
source_url = None

def configure_request(app):
    global api_key, search_url, news_url, articles_url,source_url
    api_key = app.config['API_KEY']
    news_url = app.config['ARTICLES_BASE_URL']
    source_url = app.config['SOURCES_BASE_URL']
    search_url = app.config['SEARCH_ARTICLE_BASE_URL']

def get_sources():
    '''
    '''
    with urllib.request.urlopen(source_url.format(api_key)) as url:
        data = json.loads(url.read())
        response = []
        if data['sources']:
            response=process_sources(data['sources'])
    return response

def process_sources(sources_list):
    '''
    '''
    results = []
    for item in sources_list:
        id = item.get('id')
        image = item.get('image')
        name = item.get('name')
        language = item.get('language')
        country = item.get('country')
        url = item.get('url')
        description = item.get('description')

        if item.get('id') and item.get('language')=='en':
            source_object = Sources(id,name,language,country,url,description)
            results.append(source_object)

    return results

def process_articles(articles_list):
    '''
    '''
    results = []
    for item in articles_list:
        id = item.get('id')
        title = item.get('title')
        content = item.get('content')
        image = item.get('image')
        url = item.get('url')
        urlToimage = item.get('urlToimage')
        source = item.get('source')
