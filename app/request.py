from app import app
from models import book
import urllib.request,json,xml
from models import book
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
import lxml
import re
Book= book.Book
# Getting api key
# api_key = app.config['BOOK_API_KEY']

# # Getting the movie base url
# base_url = app.config["BOOK_API_BASE_URL"]



def get_book():
    url = 'https://www.goodreads.com/search.xml?key=jCRKYMgy7fN9hxa2YlkQ&q=business'
    response = urllib.request.urlopen(url).read()
    res = bs(response, "lxml")
    # print(res)

    results = res.find('results')

    images = res.findAll('image_url')
    titles = res.findAll('title')
    authors = res.findAll('name')

    image_urls = []
    for image in images:
        clean = re.compile('<.*?>')
        clean2 = re.sub(clean, '', str(image))
        image_urls.append(clean2)

    processed_titles = []
    for title in titles:
        clean = re.compile('<.*?>')
        clean2 = re.sub(clean, '', str(title))
        processed_titles.append(clean2)

    author_names = []
    for author in authors:
        clean = re.compile('<.*?>')
        clean2 = re.sub(clean, '', str(author))
        author_names.append(clean2)


    book_results = zip(image_urls, processed_titles, author_names)
    return book_results


    
    