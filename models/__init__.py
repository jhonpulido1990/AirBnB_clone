#!/usr/bin/python3
"""Module import our FileStorage from the archived file_store"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
