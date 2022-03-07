#!/usr/bin/python3
"""Imports modules for testing"""
import os
import pycodestyle
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

    def test_style_check(self):
        """Test of pep8"""
        st = pycodestyle.StyleGuide(quiet=True)
        r = st.check_files(['models/engine/file_storage.py'])
        self.assertEqual(r.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_creation(self):
        '''
            this test validate that creation proccess was correct.
        '''
        self.assertEqual(self.storage.save(), None)

    def test_User_saveStorage(self):
        """ Checks if the save function works """
        self.usuario.first_name = "betty"
        self.usuario.save()
        self.storage.reload()
        self.storage.all()
        self.assertIsInstance(self.storage.all(), dict)
        self.assertTrue(hasattr(self.usuario, 'save'))
        self.assertNotEqual(self.usuario.created_at, self.usuario.updated_at)

    def test_file_storage_exist(self):
        """ Checks if methods exists """
        self.assertTrue(hasattr(self.storage, "all"))
        self.assertTrue(hasattr(self.storage, "new"))
        self.assertTrue(hasattr(self.storage, "save"))
        self.assertTrue(hasattr(self.storage, "reload"))

    def test_type_id(self):
        mymodel = BaseModel()
        self.assertEqual(type(mymodel.id), str)

    def test_all(self):
        """Test method All"""
        dictiona = self.storage.all()
        self.assertIsInstance(dictiona, dict)

    def test_new(self):
        """test method new"""
        s_dict = self.storage.all()
        kk = "{}.{}".format(type(self.usuario).__name__, self.usuario.id)
        self.assertTrue(kk in s_dict.keys())

    def test_save(self):
        """Test for save method"""
        path = os.getcwd()
        name_expected = 'file.json'
        try:
            os.remove(path + "/" + name_expected)
        except FileNotFoundError:
            pass

        mymodel = BaseModel()
        mymodel.save()

        dummy_dict = mymodel.to_dict()
        dummy_key = f"{mymodel.__class__.__name__}.{mymodel.id}"

        self.assertTrue(os.path.isfile(path + "/" + name_expected))
        with open(name_expected, mode="r") as file:
            output = file.read()
        dict_json = eval(output)
        keys = dict_json.keys()
        self.assertIn(dummy_key, keys)
        self.assertEqual(dummy_dict, dict_json[dummy_key])
        os.remove(path + "/" + name_expected)

    def test_reload(self):
        """Test of reload"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
