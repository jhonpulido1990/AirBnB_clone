#!/usr/bin/python3
"""
Module:
Import our FileStorage from the archived file_store
Instance create wiht name FileStora()
storage call reload() function
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
