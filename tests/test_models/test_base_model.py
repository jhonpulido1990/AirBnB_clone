#!/usr/bin/python3
"""Imports modules testers"""
import pep8
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.basemodel = BaseModel()
        cls.basemodel.first_name = 'william'
        cls.basemodel.edad = 24
        cls.basemodeldict = cls.basemodel.to_dict()
        cls.diccinary = BaseModel(**cls.basemodeldict)

    def test_atributename(self):
        """Test of atributes"""
        self.assertEqual(self.basemodel.first_name, "william")
        self.assertEqual(self.basemodel.edad, 24)

    def test_BaseModel(self):
        """Test of comprobation"""
        self.assertEqual(self.basemodel.first_name, 'william')
        self.assertTrue(self.basemodel.id)
        self.assertTrue(self.diccinary.created_at)
        self.assertNotEqual(self.basemodel.created_at,
                            self.diccinary.updated_at)
        self.assertEqual(self.basemodel.first_name,
                         self.diccinary.first_name)

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/city.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.basemodel.__doc__) > 0)

    def test_class(self):
        """value the id"""
        self.assertIsInstance(self.basemodel, BaseModel)

    def test_data(self):
        """type de data"""
        self.assertIsInstance(self.basemodeldict, dict)
        self.assertIsInstance(self.basemodel.id, str)
        self.assertIsInstance(self.basemodel.created_at, datetime)
        self.assertIsInstance(self.basemodel.__str__(), str)
        self.assertIsInstance(self.basemodel.edad, int)

    def test_save(self):
        """ saved to file. """
        self.basemodel.save()
        with open("file.json", 'r') as f:
            self.assertIn(self.basemodel.id, f.read())

    def test_to_dict(self):
        """Test of dictionary"""
        Bmodel_dict = self.basemodel.to_dict()
        self.assertEqual(self.basemodel.__class__.__name__,
                         'BaseModel')
        self.assertIsInstance(Bmodel_dict['created_at'], str)
        self.assertIsInstance(Bmodel_dict['updated_at'], str)

    def test_updated(self):
        """Test of Updated"""
        updated = self.basemodel.updated_at
        self.basemodel.save()
        self.assertTrue(self.basemodel.updated_at > updated)

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.basemodel, self.basemodeldict)


if __name__ == '__main__':
    unittest.main()
