#!/usr/bin/python3
"""Imports modules testers"""
from datetime import datetime
import unittest
import pycodestyle
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """intancia"""
        cls.amenitymodel = Amenity()
        cls.amenitymodel.name = "jhon"
        cls.amenitidict = cls.amenitymodel.to_dict()
        cls.diccinary = Amenity(**cls.amenitidict)

    def test_style_check(self):
        """Test of style"""
        st_ameni = pycodestyle.StyleGuide(quiet=True)
        stx_ameni = st_ameni.check_files(['models/amenity.py'])
        self.assertEqual(stx_ameni.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.amenitymodel.__doc__) > 0)

    def test_atribute(self):
        """validation name"""
        self.assertNotEqual(self.amenitymodel.name, "william")

    def test_amenity(self):
        """Test of comprobation"""
        self.assertEqual(self.amenitymodel.name, 'jhon')
        self.assertTrue(self.amenitymodel.id)
        self.assertTrue(self.amenitymodel.created_at)
        self.assertNotEqual(self.amenitymodel.created_at,
                            self.amenitymodel.updated_at)
        self.assertEqual(self.amenitymodel.name, self.amenitidict["name"])

    def test_data(self):
        """type de data"""
        self.assertIsInstance(self.amenitidict, dict)
        self.assertIsInstance(self.amenitymodel.id, str)
        self.assertIsInstance(self.amenitymodel.created_at, datetime)
        self.assertIsInstance(self.amenitymodel.__str__(), str)
        self.assertIsInstance(self.amenitymodel.name, str)

    def test_if_subclass(self):
        """ Tests if City is a subclass of BaseModel """
        self.assertTrue(issubclass(self.amenitymodel.__class__,
                                   BaseModel), True)

    def test_save(self):
        """ saved to file. """
        self.amenitymodel.save()
        with open("file.json", 'r') as f:
            self.assertIn(self.amenitymodel.id, f.read())

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.amenitymodel, self.amenitidict)

    def test_to_dict(self):
        """ Test to_dict method inherited from BaseModel """
        self.assertEqual('to_dict' in dir(self.amenitymodel), True)


if __name__ == '__main__':
    unittest.main()
