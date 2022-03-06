#!/usr/bin/python3
"""Imports modules for testing"""
import pep8
import unittest
import json
import os
import models
from models.engine.file_storage import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.filestorage = FileStorage()
        cls.filestorage.firts_name = 'william'
        cls.filestorage.edad = '24'

    def test_BaseModel(self):
        """Test of comprobation"""
        self.assertEqual(self.filestorage.firts_name, 'william')
        self.assertTrue(self.filestorage.id)
        self.assertTrue(self.diccinary.created_at)
        self.assertNotEqual(self.filestorage.created_at,
                            self.diccinary.updated_at)
        self.assertEqual(self.filestorage.firts_name, self.diccinary.firts_name)

    def test_pep8(self):
        """Test of pep8"""
        st = pep8.StyleGuide(quiet=True)
        r = st.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Documentation(self):
        """Test of documentation"""
        self.assertTrue(len(self.filestorage__doc__) > 0)


if __name__ == '__main__':
    unittest.main()
