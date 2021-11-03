import unittest
from models import news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = news(1234,'Hotline Blink Discovery','CNN updates','https://image.tmdb.org/t/p/w500/khsjha27hbs','politics','intresting')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,news))


if __name__ == '__main__':
    unittest.main()