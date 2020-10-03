class Book:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,author,poster,publisher,publishedDate):
        self.id =id
        self.title = title
        self.author=author
        # self.poster = 'http://books.google.com/books/content?id=_oG_iTxP1pIC&printsec=frontcover&img=1&zoom=5&source=gbs_api'+ poster
        self.publisher= publisher
        self.publishedDate=publishedDate