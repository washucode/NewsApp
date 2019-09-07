import unittest
from app import models

class testSources(unittest.TestCase):
    '''
    Test case to test behaivour of the Sources class
    '''
    def setUp(self):
        '''
        This will run before every other test
        '''
        self.new_source = Sources('ansa','ANSA.it','Agenzia ANSA: ultime notizie, foto, video e approfondimenti su...','http://www.ansa.it','general','it','it')