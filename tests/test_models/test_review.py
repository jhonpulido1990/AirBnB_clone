#!/usr/bin/python3
"""Imports modules testers"""

import unittest
import pep8
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.Reviewmodel = Review()
        cls.Reviewmodel.place_id = "cartagena"

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/review.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.Reviewmodel.__doc__) > 0)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.Reviewmodel.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.Reviewmodel is not None)

    def test_atribute(self):
        """validation place"""
        self.assertEqual(self.Reviewmodel.place_id, "cartagena")
