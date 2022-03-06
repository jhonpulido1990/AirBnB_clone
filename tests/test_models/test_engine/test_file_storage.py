#!/usr/bin/python3
"""Imports modules for testing"""
import pep8
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Testing"""

    def setUp(self):
        self.storage = FileStorage()
        self.usuario = User()

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

    def test_User_saveStorage(self):
        """ Checks if the save function works """
        self.usuario.first_name = "betty"
        self.usuario.save()
        self.storage.reload()
        self.storage.all()
        self.assertIsInstance(self.storage.all(), dict)
        self.assertTrue(hasattr(self.usuario, 'save'))
        self.assertNotEqual(self.usuario.created_at, self.usuario.updated_at)


if __name__ == '__main__':
    unittest.main()
