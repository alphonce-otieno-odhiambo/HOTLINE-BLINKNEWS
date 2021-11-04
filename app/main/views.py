from flask import render_template
from . import main
from ..request import get_news
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news = get_news()
    title = 'HOTLINE BLINKNEWS'
    return render_template('index.html', title = title,articles = news)