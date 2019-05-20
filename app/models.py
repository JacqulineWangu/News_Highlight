class Articles:
    '''
    '''
    def __init__(self, id, title, content, image, url, urlToImage, source):
        self.id = id
        self.title = title
        self.content = content
        self.image = image
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