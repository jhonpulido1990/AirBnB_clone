#!/usr/bin/python3
"""Imports modules for testing"""
import unittest
from models.engine.file_storage import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Testing"""

    def setUp(self):
        self.storage = FileStorage()

    def test_creation(self):
        '''
            this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.storage.save(), None)
