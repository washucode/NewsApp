from flask import render_template
from . import main
from ..request import news,news_article
from ..models import Sources,News_Articles



#actual views

@main.route('/')
def index():
    general = news()
    
    return render_template("index.html",general=general)

@main.route('/sources/<id>')
def articles(id):
	'''
	view  page with articles
	'''
	articles = news_article(id)
	source = id 
	sources = news()
	title = None
	for source_item in sources:
		if source == source_item.id:
			title = source_item.name
			slogan = source_item.description


	return render_template('news.html',articles = articles,source=source,title=title,slogan=slogan)