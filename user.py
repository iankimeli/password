'''
User Module by Carol Wanjohi

Import Credential from credential module to access an account's credentials
'''
from credential import Credential

'''
User class : for creating a password locker account
'''

class User:
    '''
    Class that generates instances of user accounts
    '''

    # Empty list of users
    user_list = []

    def __init__(self, user_name, user_password):
        '''
        __init__ method to define the properties of a User object

        Args:
            user_name : name of a user
            user_password : password for a user
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        '''
        Method that saves a user to user list
        '''
        User.user_list.append(self)


    @classmethod
    def find_credential(cls, name):
        '''
        Method that checks if Credentials is imported correctly

        Args:
            name : name of the credential

        Returns:
            Boolean : True / False if the credential exists or does not exist
        '''

        # Search for the user in the user list
        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        '''
        Method that allows a user to log into their credential

        Args:
            name : name of the user
            password : password for the user

        Returns:
            Credential list for the user that matches the name and password
            False: if the name or password is incorrect
        '''
