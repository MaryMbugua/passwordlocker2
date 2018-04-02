import string
import secrets
import random
import pyperclip

class Credentials:
    '''
    CLASS THAT GENERATES A NEW INSTANCE OF A USER/
    CREATES A NEW ACCOUNT
    '''
    credential_list = []
    def __init__(self,app_name,account_name,account_password):
        '''
        initialises a new instance of a credential
        '''
        self.app_name = app_name
        self.account_name = account_name
        self.account_password= account_password
    def save_newcredential(self):
        Credentials.credential_list.append(self)