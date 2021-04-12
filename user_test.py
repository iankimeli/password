'''
User Test by Ian Kimeli

import uniittest to create uniittests for User Module
import User Module to be tested
'''
import unittest
from user import User
from credential import Credential


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create user object
        self.new_user = User("John","doe")


