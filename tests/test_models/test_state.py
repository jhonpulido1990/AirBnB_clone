#!/usr/bin/python3
"""Imports modules testers"""
import unittest
from datetime import datetime
import pycodestyle
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.statemodel = State()
        cls.statemodel.name = "william"
        cls.statemodeldict = cls.statemodel.to_dict()
        cls.diccinary = State(**cls.statemodeldict)

    def test_style_check(self):
        """Test of style"""
        st = pycodestyle.StyleGuide(quiet=True)
        stx = st.check_files(['models/base_model.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.statemodel.__doc__) > 0)

    def test_atributename(self):
        """validation name"""
        self.assertEqual(self.statemodel.name, "william")

    def test_city(self):
        """Test of comprobation"""
        self.assertEqual(self.statemodel.name, 'william')
        self.assertTrue(self.statemodel.id)
        self.assertTrue(self.statemodel.created_at)
        self.assertNotEqual(self.statemodel.created_at,
                            self.statemodel.updated_at)
        self.assertEqual(self.statemodel.name, self.statemodeldict["name"])

    def test_data(self):
        """type de data"""
        self.assertIsInstance(self.statemodeldict, dict)
        self.assertIsInstance(self.statemodel.id, str)
        self.assertIsInstance(self.statemodel.created_at, datetime)
        self.assertIsInstance(self.statemodel.__str__(), str)
        self.assertIsInstance(self.statemodel.name, str)

    def test_if_subclass(self):
        """ Tests if City is a subclass of BaseModel """
        self.assertTrue(issubclass(self.statemodel.__class__, BaseModel), True)

    def test_save(self):
        """ saved to file. """
        self.statemodel.save()
        with open("file.json", 'r') as f:
            self.assertIn(self.statemodel.id, f.read())

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.statemodel, self.statemodeldict)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.statemodel), True)


if __name__ == '__main__':
    unittest.main()
