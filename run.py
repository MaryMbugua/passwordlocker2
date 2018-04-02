#!/usr/bin/env pythn3.6
from user import User
from credentials import Credentials


        ####USER

##creating a user
def create_user(fname,lname,uname,phone,email,passw):
    new_user = User(fname,lname,uname,phone,email,passw)
    return new_user
##save users
def save_user(user):
    user.save_user()
#displaying all users
def display_allusers():
    return User.display_allusers()
#generate a random password
def generate_randompass():
    return User.generate_randompass()

 ######CREDENTIALS

##creating a new credential
def create_credential(apname,acname,psname):
    new_credential = Credentials(apname,acname,psname)
    return new_credential
##save credential
def save_newcredential(credentials):
    credentials.save_newcredential()
##delete a credential
def deletecredential(credentials):
    credentials.deletecredential()
##finding a password using appname
def find_credentialbyappname(credentials):
    return Credentials.find_credentialbyappname(credentials)
##check if credential exists
def credential_exist(appname):
    return Credentials.credential_exist(appname)
###displaying all credentials
def display_allcredentials():
    return Credentials.display_allcredentials()