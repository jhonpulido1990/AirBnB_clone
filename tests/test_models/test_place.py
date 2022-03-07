#!/usr/bin/python3
"""Imports modules testers"""
from datetime import datetime
import unittest
import pycodestyle
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """instance"""
        cls.placemodel = Place()
        cls.placemodel.number_rooms = 1
        cls.placemodel.city_id = 'Cali'
        cls.placemodel.user_id = '1516dgb1d'
        cls.placemodel.name = 'william'
        cls.placemodel.description = 'sensey'
        cls.placemodel.number_bathrooms = 2
        cls.placemodel.max_guest = 5
        cls.placemodel.price_by_night = 3
        cls.placemodel.latitude = 5.8
        cls.placemodel.longitude = 6.7
        cls.placemodel.amenity_ids = ["cali", "medellin", "bogota"]
        cls.placedict = cls.placemodel.to_dict()
        cls.diccinary = Place(**cls.placedict)

    def test_style_check(self):
        """Test of style"""
        st = pycodestyle.StyleGuide(quiet=True)
        stx = st.check_files(['models/place.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.placemodel.__doc__) > 0)

    def test_Data(self):
        """validation number"""
        self.assertIsInstance(self.placemodel.number_bathrooms, int)
        self.assertIsInstance(self.placemodel.city_id, str)
        self.assertIsInstance(self.placemodel.user_id, str)
        self.assertIsInstance(self.placemodel.name, str)
        self.assertIsInstance(self.placemodel.description, str)
        self.assertIsInstance(self.placemodel.number_rooms, int)
        self.assertIsInstance(self.placemodel.max_guest, int)
        self.assertIsInstance(self.placemodel.price_by_night, int)
        self.assertIsInstance(self.placemodel.longitude, float)
        self.assertIsInstance(self.placemodel.latitude, float)
        self.assertIsInstance(self.placemodel.amenity_ids, list)
        self.assertIsInstance(self.placemodel.created_at, datetime)
        self.assertIsInstance(self.placedict, dict)
        self.assertIsInstance(self.placemodel.id, str)
        self.assertIsInstance(self.placemodel.__str__(), str)

    def test_atributename(self):
        """validation name"""
        self.assertEqual(self.placemodel.city_id, "Cali")
        self.assertEqual(self.placemodel.name, "william")
        self.assertEqual(self.placemodel.description, "sensey")
        self.assertNotEqual(self.placemodel.user_id, "fb15sv1v11fb11vv11v")
        self.assertEqual(self.placemodel.number_bathrooms, 2)
        self.assertNotEqual(self.placemodel.amenity_ids, [])
        self.assertNotEqual(self.placemodel.price_by_night, 4)
        self.assertNotEqual(self.placemodel.number_rooms, 2)

    def test_if_subclass(self):
        """ Tests if City is a subclass of BaseModel """
        self.assertTrue(issubclass(self.placemodel.__class__, BaseModel), True)

    def test_place(self):
        """Test of comprobation"""
        self.assertEqual(self.placemodel.name, 'william')
        self.assertTrue(self.placemodel.id)
        self.assertTrue(self.placemodel.created_at)
        self.assertNotEqual(self.placemodel.created_at,
                            self.placemodel.updated_at)
        self.assertEqual(self.placemodel.name, self.placedict["name"])

    def test_save(self):
        """ saved to file."""
        self.placemodel.save()
        with open("file.json", 'r') as f:
            self.assertIn(self.placemodel.id, f.read())

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.placemodel, self.placedict)


if __name__ == '__main__':
    unittest.main()
