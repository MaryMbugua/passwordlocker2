import string
import secrets
import random
import pyperclip

class User:
    '''
    CLASS THAT GENERATES A NEW INSTANCE OF A USER/
    CREATES A NEW ACCOUNT
    '''
    user_list = []
    def __init__(self,first_name,last_name,user_name,phone_number,email,password):
        '''
        initialises a new instance of a credential
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.password= password
    def save_user(self):
        User.user_list.append(self)
    @classmethod
    def display_allusers(cls):
        '''
        method that returns the userslist
        '''
        return cls.user_list
