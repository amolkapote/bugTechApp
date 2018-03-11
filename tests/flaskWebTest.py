'''
@author: AK
@summary: Unit test to validate status of 'List Bugs', 'Add Bug', 'List Users', 'Add User' pages
'''
import unittest
from app import app


class FlaskWebTest(unittest.TestCase):


    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
    
    def test_add_bug_page_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/new_bug') 
        
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
    def test_bugs_page_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/bugs') 
        
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
    def test_add_user_page_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/new_contact') 
        
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
    def test_users_page_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/contacts') 
        
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
        
        

    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()