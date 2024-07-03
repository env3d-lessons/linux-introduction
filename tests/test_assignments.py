import pathlib
import os

files = ['TSLA.csv', 'tesla.db', 'schema.sql', 'import.sql']

def test_files_exist():
    # Test for the presence of various files
    for f in files:
        assert pathlib.Path(f).is_file()

def test_file_size():
    for f in files:
        assert pathlib.Path(f).stat().st_size > 0



