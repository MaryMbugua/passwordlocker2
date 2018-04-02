import unittest ##import unittest module
from credentials import Credentials ##import credential class from credentials.py file
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_credential = Credentials("facebook","berylmmbone","mypass") #create user object
    def tearDown(self):
        '''
        cleans up after each test case has 
        been executed
        '''
        Credentials.credential_list = []
