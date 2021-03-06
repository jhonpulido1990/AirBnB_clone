#!/usr/bin/python3
"""Imports modules tester"""
import unittest
from models.user import User
import pycodestyle
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """intance"""
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

    def test_pycodestyle(self):
        """Test of style"""
        st = pycodestyle.StyleGuide(quiet=True)
        stx = st.check_files(['models/user.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.user.__doc__) > 0)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.user.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.user is not None)


if __name__ == '__main__':
    unittest.main()
