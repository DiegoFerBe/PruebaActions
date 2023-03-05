import enum

from sqlalchemy import Column, Integer, String, Enum
from .declarative_base import Base


class Tipo(enum.Enum):
    LOGIN = 1
    TARJETA = 2
    SECRETO = 3
    ID = 4


class Elemento(Base):
    __tablename__ = 'elementos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo = Column(Enum(Tipo))
    nota = Column(String)
