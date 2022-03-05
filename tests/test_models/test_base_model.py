#!/usr/bin/python3

import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basemodel = BaseModel()
        cls.basemodel.firts_name = 'william'
        cls.basemodel.edad = '24'
        cls.basemodeldict = cls.basemodel.to_dict()
        cls.diccinary = BaseModel(**cls.basemodeldict)

    def test_BaseModel(self):
        self.assertEqual(self.basemodel.firts_name, 'william')
        self.assertTrue(self.basemodel.id)
        self.assertTrue(self.diccinary.created_at)
        self.assertNotEqual(self.basemodel.created_at, self.diccinary.updated_at)
        self.assertEqual(self.basemodel.firts_name, self.diccinary.firts_name)
        self.assertEqual(type(self.basemodel.created_at), type(BaseModel().created_at))

    

if __name__ == '__main__':
    unittest.main()
