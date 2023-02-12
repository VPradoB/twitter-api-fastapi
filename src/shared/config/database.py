import os
from uuid import UUID

from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing_extensions import Annotated

sqlite_file_name = 'database.db'

base_dir = os.path.dirname(os.path.realpath(__file__))
sqlite_file_path = os.path.join(base_dir, sqlite_file_name)

database_url = f'sqlite:///{sqlite_file_path}'

engine = create_engine(database_url, echo=True, connect_args={"check_same_thread": False})

session = sessionmaker(bind=engine)()


class BaseModel(DeclarativeBase):
    uuid_pk = Annotated[UUID, 'primary_key']
    str50 = Annotated[str, 50]
    type_annotation_map = {
        str50: String(50),
    }
    pass
