#!/usr/bin/python3
"""Imports modules for testing"""
import pycodestyle
import unittest
import json
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Testing"""

    def test_pycodestyle(self):
        """Test of pycodestyle"""
        st = pycodestyle.StyleGuide(quiet=True)
        r = st.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Documentation(self):
        """Test of documentation"""
        self.assertTrue(len(models.engine.file_storage.__doc__) > 0)
