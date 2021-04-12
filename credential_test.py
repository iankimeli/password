'''
Password Locker Test by Carol Wanjohi

import uniittest to create uniittests for Password Locker Module
import Password Locker Module to be tested
'''
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the Credential Class behaviours

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        # Create credential object
        self.new_credential = Credential("doe","Yahoo","yahoo17")

