import os


class Config:
    SEARCH_BASE_URL ='https://newsapi.org/v2/sources?language=en&category&apiKey={}'
    SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWSARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}