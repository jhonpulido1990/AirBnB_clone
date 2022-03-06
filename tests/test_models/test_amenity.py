#!/usr/bin/python3
"""Imports modules testers"""

import unittest
import pep8
import os
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """intancia"""
        cls.amenitymodel = Amenity()
        cls.amenitymodel.name = "jhon"

    def test_pep8(self):
        """Test of style"""
        st_ameni = pep8.StyleGuide(quiet=True)
        stx_ameni = st_ameni.check_files(['models/amenity.py'])
        self.assertEqual(stx_ameni.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.amenitymodel.__doc__) > 0)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.amenitymodel.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.amenitymodel is not None)

    def test_atribute(self):
        """validation name"""
        self.assertNotEqual(self.amenitymodel.name, "william")


if __name__ == '__main__':
    unittest.main()
