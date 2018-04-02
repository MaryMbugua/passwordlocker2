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
    def test_save_multiplecredential(self):
        '''
        to test if we can save multiple credentials
        to the credential list
        '''
        self.new_credential.save_newcredential()
        test_credential = Credentials("testapp","testuser","testpass")
        test_credential.save_newcredential()
        self.assertEqual(len(Credentials.credential_list),2)
    def test_deletecredential(self):
        '''
        to test if we can delete a credential
        from our credential list
        '''
        self.new_credential.save_newcredential()
        test_credential = Credentials("testapp","testuser","testpass")
        test_credential.save_newcredential()
        self.new_credential.deletecredential()
        self.assertEqual(len(Credentials.credential_list),1)
    def test_find_credentialbyappname(self):
        '''
        test to check if we can find a credential by using
        the application name and display information
        '''
        self.new_credential.save_newcredential()
        test_credential = Credentials("newapp","testuser","testpass")
        test_credential.save_newcredential()
        found_credential = Credentials.find_credentialbyappname("newapp")
        self.assertEqual(found_credential.account_name,test_credential.account_name)