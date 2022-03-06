#!/usr/bin/python3
"""Imports modules testers"""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.basemodel = BaseModel()
        cls.basemodel.firts_name = 'william'
        cls.basemodel.edad = 24
        cls.basemodeldict = cls.basemodel.to_dict()
        cls.diccinary = BaseModel(**cls.basemodeldict)

    def test_BaseModel(self):
        """Test of comprobation"""
        self.assertEqual(self.basemodel.firts_name, 'william')
        self.assertTrue(self.basemodel.id)
        self.assertTrue(self.diccinary.created_at)
        self.assertNotEqual(self.basemodel.created_at,
                            self.diccinary.updated_at)
        self.assertEqual(self.basemodel.firts_name,
                         self.diccinary.firts_name)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.basemodel.id
        self.assert_(result is not None)

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

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.basemodel, self.basemodeldict)


if __name__ == '__main__':
    unittest.main()
