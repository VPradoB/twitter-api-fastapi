import glob
import importlib
import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

logger = logging.getLogger(os.getenv('LOGGER_NAME'))


class Base(DeclarativeBase):
    pass

class Database:
    engine = None
    session = None
    metadata = None

    @classmethod
    def create_database_sqlite(cls, database_url: str):
        cls.engine = create_engine(database_url, echo=True, connect_args={"check_same_thread": False})
        cls.import_tables_module()
        Base.metadata.create_all(bind=cls.engine)

    @staticmethod
    def import_tables_module():
        path = 'src/*/infrastructure/database/*_table.py'
        for filename in glob.glob(path):
            module = filename.replace('/', '.').replace('\\', '.')[:-3]
            table = importlib.import_module(module)
