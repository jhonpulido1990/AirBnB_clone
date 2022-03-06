#!/usr/bin/python3
"""Imports modules testers"""

import unittest
import pep8
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.placemodel = Place()
        cls.placemodel.number_rooms = 1

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/place.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.placemodel.__doc__) > 0)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.placemodel.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.placemodel is not None)

    def test_atribute(self):
        """validation number"""
        self.assertIsInstance(self.placemodel.number_bathrooms, int)


if __name__ == '__main__':
    unittest.main()
