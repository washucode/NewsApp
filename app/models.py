class Sources:
    '''
    class to define Sources instances
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language

class News_Articles:
    '''
    class to define Sources instances
    '''

    def __init__(self,id,author,title,description,url,urlToImage,publishedAt):
    
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt