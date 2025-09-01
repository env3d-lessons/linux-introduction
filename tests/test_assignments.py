import pathlib
import os

def test_TSLA_csv_exists():
    assert pathlib.Path('TSLA.csv').is_file()

def test_tesla_db_exists():
    assert pathlib.Path('tesla.db').is_file()

def test_schema_sql_exists():
    assert pathlib.Path('schema.sql').is_file()

def test_import_sql_exists():
    assert pathlib.Path('import.sql').is_file()

def test_TSLA_csv_size():
    assert pathlib.Path('TSLA.csv').stat().st_size > 0

def test_tesla_db_size():
    assert pathlib.Path('tesla.db').stat().st_size > 0

def test_schema_sql_size():
    assert pathlib.Path('schema.sql').stat().st_size > 0

def test_import_sql_size():
    assert pathlib.Path('import.sql').stat().st_size > 0



