import os

from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'database.sqlite'))

engine = create_engine(f'sqlite:///{database}')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()



