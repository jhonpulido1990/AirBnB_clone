#!/usr/bin/python3
"""Imports modules testers"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.basemodel = BaseModel()
        cls.basemodel.firts_name = 'william'
        cls.basemodel.edad = '24'
        cls.basemodeldict = cls.basemodel.to_dict()
        cls.diccinary = BaseModel(**cls.basemodeldict)

    def test_BaseModel(self):
        """Test of comprobation"""
        self.assertEqual(self.basemodel.firts_name, 'william')
        self.assertTrue(self.basemodel.id)
        self.assertTrue(self.diccinary.created_at)
        self.assertNotEqual(self.basemodel.created_at,
                            self.diccinary.updated_at)
        self.assertEqual(self.basemodel.firts_name, self.diccinary.firts_name)

    def test_MethodExists(self):
        """ Does MyMethod() exist?"""
        result = self.basemodel.id
        self.assert_(result is not None)

    def test_ClassExists(self):
        """ Does the class exist? """
        self.assert_(self.basemodel is not None)
