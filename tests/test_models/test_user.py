#!/usr/bin/python3
"""Imports modules tester"""
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.first_name = 'William'
        cls.user.last_name = 'Cardozo'
        cls.user.edad = '24'
        cls.user.email = ''
        cls.user.password = ''
        cls.userdict = cls.user.to_dict()
        cls.diccinary = User(**cls.userdict)

    def test_User(self):
        """Test of comprobation"""
        self.assertEqual(self.user.first_name, 'William')


if __name__ == '__main__':
    unittest.main()
