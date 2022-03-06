#!/usr/bin/python3
"""Imports modules for testing"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing"""
    def something(self):
        self.do_something()


if __name__ == "__main__":
    unittest.main()
