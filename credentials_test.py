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
    def test_init(self):
        '''
        to test if object is initialised properly
        '''
        self.assertEqual(self.new_credential.app_name,"facebook")
        self.assertEqual(self.new_credential.account_name,"berylmmbone")
        self.assertEqual(self.new_credential.account_password,"mypass")
    def test_save_newcredential(self):
        '''
        to test if credential object is saved
         into credential list
        '''
        self.new_credential.save_newcredential()
        self.assertEqual(len(Credentials.credential_list),1)