import requests
from .models import Sources, News_Article


base_news_url = None
base_articles_url = None
api_key = None
  
def configure_request(app):
	global api_key,base_news_url,base_articles_url
	api_key = app.config['NEWS_API_KEY']
	base_news_url = app.config['SOURCES_BASE_URL']
	base_articles_url = app.config['NEWSARTICLES_BASE_URL']
    


def news(category):
    source_url = base_news_url.format(category,api_key)
    my_sources = requests.get(source_url).json()
    my_results = my_sources['sources']
    
  
    my_final_sources = []

    
    for source in my_results :
        id = source['id']
        name = source['name']
        description = source['description']
        url = source['url']
        category = source['category']
        language = source['language']
        country = source['country']

        sources_object = Sources(id,name,description,url,category,country,language)
        my_final_sources.append(sources_object)


    return my_final_sources

def news_article(id):
    source_url = base_articles_url.format(id,api_key)
    my_article = requests.get(source_url).json()
    my_results = my_article['articles']
    
  
    my_final_article = []

    
    for article in my_results :
        id = article['id']
		author = article['author']
		title = article['title']
		description = article['description']
		url = article['url']
		urlToImage = article['urlToImage']
		publishedAt = article['publishedAt']

        articles_object = News_Article(id,author,title,description,url,urlToImage,publishedAt)
        my_final_article.append(articless_object)


    return my_final_sources
        

