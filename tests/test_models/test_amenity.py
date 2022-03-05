#!/usr/bin/python3
"""Imports modules testers"""

import unittest
import pep8
import os
import models
from models.engine.file_storage import FileStorage
from models.user import User


class TestAmenity(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """intancia"""
        cls.usermodel = User()

    def test_pep8(self):
        """Test of style"""
        st_ameni = pep8.StyleGuide(quiet=True)
        stx_ameni = st_ameni.check_files(['models/amenity.py'])
        self.assertEqual(stx_ameni.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.usermodel.__doc__) > 0)


if __name__ == '__main__':
    unittest.main()
