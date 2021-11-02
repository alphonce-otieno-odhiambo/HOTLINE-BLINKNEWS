from flask import render_template
from app import app

@app.route('/')
def index():
    title = 'Welcome to Hotline Blink News'
    return render_template('index.html',title = title)

@app.route('/article/article_id')
def article(article_id):
    '''views that returns the article pages news with its data'''
    return render_template('article.html', id = article_id)