import unittest
from app.models import  Sources,News_Articles

class testSources(unittest.TestCase):
    '''
    Test case to test behaivour of the Sources class
    '''
    def setUp(self):
        '''
        This will run before every other test
        '''
        self.new_source = Sources('ansa','ANSA.it','Agenzia ANSA: ultime notizie, foto, video e approfondimenti su...','http://www.ansa.it','general','it','it')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_checkinstancevariables(self):
        self.assertEquals(self.new_source.id,'ansa')
        self.assertEquals(self.new_source.name,'ANSA.it')
        self.assertEquals(self.new_source.description,'Agenzia ANSA: ultime notizie, foto, video e approfondimenti su...')
        self.assertEquals(self.new_source.url,'http://www.ansa.it')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'it')
        self.assertEquals(self.new_source.language,'it')
    
class testNewsArticles(unittest.TestCase):


    def setUp(self):

        self.new_Article = News_Articles('techcrunch','Anthony Ha','Daily Crunch: Apple Music comes to the web',"The Daily Crunch is TechCrunch’s roundup of our biggest...","http://techcrunch.com/2019/09/06/daily-crunch-apple-music-comes-to-the-web/","https://techcrunch.com/wp-content/uploads/2019/09/browse-signed-in-MBP.jpeg?w=618","2019-09-06T18:39:13Z")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_Article,News_Articles))

    def test_checkinstancevariables(self):
        self.assertEquals(self.new_Article.id,'techcrunch')
        self.assertEquals(self.new_Article.author,'Anthony Ha')
        self.assertEquals(self.new_Article.title,'Daily Crunch: Apple Music comes to the web')
        self.assertEquals(self.new_Article.description,"The Daily Crunch is TechCrunch’s roundup of our biggest...")
        self.assertEquals(self.new_Article.url,"http://techcrunch.com/2019/09/06/daily-crunch-apple-music-comes-to-the-web/")
        self.assertEquals(self.new_Article.urlToImage,"https://techcrunch.com/wp-content/uploads/2019/09/browse-signed-in-MBP.jpeg?w=618")
        self.assertEquals(self.new_Article.publishedAt,'2019-09-06T18:39:13Z')


     

