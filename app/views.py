from flask import render_template
from app import app
from .request import  get_book

# Views
@app.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    book= get_book()
    title = 'title'
    
    return render_template('index.html',books=book, title=title)
@app.route('/book/<int:id>')
def get_books(id):

    '''
    View book page function that returns the movie details page and its data
    '''
    book= get_books(id)
    title = f'{book.title}'

    return render_template('book.html',title=title,book=book)