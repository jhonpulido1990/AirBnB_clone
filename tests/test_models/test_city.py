#!/usr/bin/python3
"""Imports modules testers"""
from datetime import datetime
import unittest
import pep8
from models.city import City


class TestCity(unittest.TestCase):
    """Testing"""

    @classmethod
    def setUpClass(cls):
        """starting"""
        cls.citymodel = City()
        cls.citymodel.name = "william"
        cls.citymodel.state_id = "fb15sv1v11fb11vv11v"
        cls.citymodeldict = cls.citymodel.to_dict()
        cls.diccinary = City(**cls.citymodeldict)

    def test_pep8(self):
        """Test of style"""
        st = pep8.StyleGuide(quiet=True)
        stx = st.check_files(['models/city.py'])
        self.assertEqual(stx.total_errors, 0, "check pep8")

    def test_docstring(self):
        """Test of docstring"""
        self.assertTrue(len(self.citymodel.__doc__) > 0)

    def test_atributename(self):
        """validation name"""
        self.assertEqual(self.citymodel.name, "william")
        self.assertEqual(self.citymodel.state_id, "fb15sv1v11fb11vv11v")

    def test_amenity(self):
        """Test of comprobation"""
        self.assertEqual(self.citymodel.name, 'william')
        self.assertTrue(self.citymodel.id)
        self.assertTrue(self.citymodel.created_at)
        self.assertNotEqual(self.citymodel.created_at,
                            self.citymodel.updated_at)
        self.assertEqual(self.citymodel.name, self.citymodeldict["name"])

    def test_data(self):
        """type de data"""
        self.assertIsInstance(self.citymodeldict, dict)
        self.assertIsInstance(self.citymodel.id, str)
        self.assertIsInstance(self.citymodel.created_at, datetime)
        self.assertIsInstance(self.citymodel.__str__(), str)
        self.assertIsInstance(self.citymodel.name, str)

    def test_save(self):
        """ saved to file. """
        self.citymodel.save()
        with open("file.json", 'r') as f:
            self.assertIn(self.citymodel.id, f.read())

    def test_Kwarg(self):
        """validation the Kwarg"""
        self.assertNotEqual(self.citymodel, self.citymodeldict)


if __name__ == '__main__':
    unittest.main()
