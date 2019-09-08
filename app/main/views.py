from flask import render_template
from . import main
from ..request import news
from ..models import Sources



#actual views

@main.route('/')
def index():
    general = news('general')
    sports = news('sports')
    technology= news('technology')
    entertainment = news('entertainment')
    return render_template("index.html",general=general,sports=sports,technology=technology,entertainment=entertainment)

