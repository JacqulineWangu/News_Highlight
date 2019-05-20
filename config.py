import os

class Config:
    '''
    '''
    API_KEY = os.environ.get('API_KEY')
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SEARCH_ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    
class DevConfig(Config):
    '''
    '''
    DEBUG = True

class ProdConfig(Config):
    '''
    '''
    pass


config_options={
    'development':DevConfig,
    'production':ProdConfig
}
