class Config:
    '''
    General configuration parent class
    '''
    BOOK_API_BASE_URL='https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key={}'
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True