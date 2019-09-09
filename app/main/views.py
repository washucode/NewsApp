from flask import render_template
from . import main
from ..request import news,news_article
from ..models import Sources,News_Articles



#actual views

@main.route('/')
def index():
    general = news('general')
    sports = news('sports')
    technology= news('technology')
    entertainment = news('entertainment')
    return render_template("index.html",general=general,sports=sports,technology=technology,entertainment=entertainment)

@main.route('/sources/<id>')
def articles(id):
	'''
	view  page with articles
	'''
	articles = news_article(id)
	source = id

	return render_template('news.html',articles = articles,source=source)