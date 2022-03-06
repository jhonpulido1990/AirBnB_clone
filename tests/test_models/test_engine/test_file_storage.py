#!/usr/bin/python3
"""Imports modules for testing"""
import pep8
import unittest
import json
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

    def test_pep8(self):
        """Test of pep8"""
        st = pep8.StyleGuide(quiet=True)
        r = st.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
