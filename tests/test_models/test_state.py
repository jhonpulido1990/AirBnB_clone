#!/usr/bin/python3
"""Imports modules testers"""

import unittest
import pep8
import os
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.statemodel = State()
        cls.statemodel.name = "william"

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/base_model.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.statemodel.__doc__) > 0)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.statemodel.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.statemodel is not None)

    def test_atribute(self):
        """validation name"""
        self.assertEqual(self.statemodel.name, "william")


if __name__ == '__main__':
    unittest.main()
