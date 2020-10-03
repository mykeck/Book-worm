import unittest
from models import book
Book= book.Book

class BookTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Book class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_book = Book(1234,'LORD of the rings','A thrilling new book','"http://books.google.com/books/content?id=_oG_iTxP1pIC&printsec=frontcover&img=1&zoom=5&source=gbs_api"',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_book,Book))


if __name__ == '__main__':
    unittest.main()