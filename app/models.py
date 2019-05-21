class Articles:
    '''
    '''
    def __init__(self, title, content, url, urlToImage, source):
        self.title = title
        self.content = content
        self.url = url
        self.urlToImage = urlToImage
        self.source = source

class Sources:
    '''
    '''
    def __init__(self, id, name, language, country, url, description):
        self.id = id
        self.name = name
        self.language = language
        self.country = country
        self.url = url
        self.description = description