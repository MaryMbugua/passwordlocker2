import unittest ##import unittest module
from user import User ##import user class from user.py file
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_user = User("mary","mbugua","nish","0789755096","mary@gmail.com","lovepy") #create user object
    def tearDown(self):
        '''
        cleans up after each test case has 
        been executed
        '''
        User.user_list = []