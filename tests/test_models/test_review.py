#!/usr/bin/python3
"""Imports modules testers"""
import unittest
from datetime import datetime
import pycodestyle
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.Reviewmodel = Review()
        cls.Reviewmodel.place_id = "cartagena"
        cls.Reviewmodel.user_id = "333cdt445"
        cls.Reviewmodel.text = ""
        cls.Reviewmodeldict = cls.Reviewmodel.to_dict()
        cls.diccinary = Review(**cls.Reviewmodeldict)

    def test_style_check(self):
        """Test of style"""
        st = pycodestyle.StyleGuide(quiet=True)
        stx = st.check_files(['models/review.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.Reviewmodel.__doc__) > 0)

    def test_atributename(self):
        """validation place"""
        self.assertEqual(self.Reviewmodel.text, "")
        self.assertEqual(self.Reviewmodel.user_id, "333cdt445")
        self.assertEqual(self.Reviewmodel.place_id, "cartagena")

    def test_Review(self):
        """Test of comprobation"""
        self.assertEqual(self.Reviewmodel.place_id, 'cartagena')
        self.assertTrue(self.Reviewmodel.id)
        self.assertTrue(self.Reviewmodel.created_at)
        self.assertNotEqual(self.Reviewmodel.created_at,
                            self.Reviewmodel.updated_at)
        self.assertEqual(self.Reviewmodel.place_id,
                         self.Reviewmodeldict["place_id"])

    def test_data(self):
        """type de data"""
        self.assertIsInstance(self.Reviewmodeldict, dict)
        self.assertIsInstance(self.Reviewmodel.id, str)
        self.assertIsInstance(self.Reviewmodel.created_at, datetime)
        self.assertIsInstance(self.Reviewmodel.__str__(), str)
        self.assertIsInstance(self.Reviewmodel.place_id, str)

    def test_save(self):
        """ saved to file. """
        self.Reviewmodel.save()
        with open("file.json", 'r') as f:
            self.assertIn(self.Reviewmodel.id, f.read())

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.Reviewmodel, self.Reviewmodeldict)


if __name__ == '__main__':
    unittest.main()
