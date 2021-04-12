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



    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''

        User.user_list = []

    def test_init(self):
        '''
        Test case to test if the object is initialised properly
        '''

        self.assertEqual( self.new_user.user_name, "John" )
        self.assertEqual( self.new_user.user_password, "doe" )

    def test_save_user(self):
        '''
        Test case to test if the user object is saved into the user list
        '''
