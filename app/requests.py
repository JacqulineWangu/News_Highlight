import urllib.request, json
from .models import Sources, Articles

api_key = None
search_url = None
news_url = None
articles_url = None
source_url = None
news_by_source = None
search_url = None

def configure_request(app):
    global api_key, search_url, news_url, articles_url, source_url, news_by_source
    api_key = app.config['API_KEY']
    news_url = app.config['ARTICLES_BASE_URL']
    source_url = app.config['SOURCES_BASE_URL']
    search_url = app.config['SEARCH_ARTICLE_BASE_URL']
    news_by_source = app.config['NEW_BY_SOURCE']

def get_sources():
    '''
    '''
    with urllib.request.urlopen(source_url.format(api_key)) as url:
        data = json.loads(url.read())
        response = []
        if data['sources']:
            response=process_sources(data['sources'])
    return response


def search_key(vals):
    '''
    '''
    with urllib.request.urlopen(search_url.format(vals,api_key)) as url:
        data = json.loads(url.read())
        response = []
        if data['articles']:
            response = process_articles(data['articles'])
    return response

def get_source_news(source_id):
    '''
    '''
    with urllib.request.urlopen(news_by_source.format(source_id,api_key)) as url:
        data = json.loads( url.read() )
        response = []
        if data['articles']:
            # print(data['articles'])
            response = process_articles(data['articles'])
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

def get_articles():
    '''
    '''
    with urllib.request.urlopen(news_url.format(api_key)) as url:
        data = json.loads(url.read())
        response = []
        if data['articles']:
            data_items=data['articles']
            return process_articles(data_items)
        else:
            return []
    

def process_articles(articles_list):
    '''
    '''
    results_list = []
    for item in articles_list:
        title = item.get('title')
        content = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        source = item.get('source')
        if content and urlToImage:
            article_object = Articles( title, content, url, urlToImage, source)
            results_list.append(article_object)
    return results_list