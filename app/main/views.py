from flask import render_template
from . import main



#actual views

@main.route('/')
def index():
    return render_template("index.html")

