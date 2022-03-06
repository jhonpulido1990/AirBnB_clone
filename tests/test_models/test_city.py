#!/usr/bin/python3
"""Imports modules testers"""
import unittest
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """starting"""
        cls.citymodel = City()
        cls.citymodel.name = "william"

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/city.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.citymodel.__doc__) > 0)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.citymodel.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.citymodel is not None)

    def test_atributename(self):
        """validation name"""
        self.assertEqual(self.citymodel.name, "william")
