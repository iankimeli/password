'''
Credential Module by Ian Kimeli

Import random and string modules from Python for generating passwords
# Import User from user module to get access to a user
'''
from random import choice
import string
# from user import User

'''
Credential class : for creating a credentials for a user
'''

class Credential:
    '''
    Class that generates instances of a users credentials
    '''

    # Empty list of credentials
    credential_list = []
