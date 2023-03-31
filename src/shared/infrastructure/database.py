import glob
import importlib
import logging
import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(os.getenv('LOGGER_NAME'))


class Database:
    engine = None
    session = None
    metadata = None

    @classmethod
    def create_database_sqlite(cls, database_path: str, database_name: str = 'database.sqlite'):
        sqlite_file_path = os.path.join(database_path, database_name)
        database_url = f'sqlite:///{sqlite_file_path}'
        cls.engine = create_engine(database_url, echo=True, connect_args={"check_same_thread": False})
        cls.metadata = MetaData()
        cls.session = sessionmaker(autocommit=False, autoflush=False, bind=cls.engine)()

        cls.create_tables(cls.metadata)
        cls.metadata.create_all(cls.engine)

    @staticmethod
    def create_tables(metadata):
        path = 'src/*/infrastructure/database/*_table.py'
        for filename in glob.glob(path):
            module = filename.replace('/', '.')[:-3]
            table = importlib.import_module(module)
            table.define_table(metadata)
