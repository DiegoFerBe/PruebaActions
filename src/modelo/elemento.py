import enum

from sqlalchemy import Column, Integer, String, Enum
from .declarative_base import Base


class Tipo(enum.Enum):
    LOGIN = 'Login'
    TARJETA = 'Tarjeta'
    SECRETO = 'Secreto'
    ID = 'Identificacion'


class Elemento(Base):
    __tablename__ = 'elementos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo = Column(Enum(Tipo))
    nota = Column(String)

    def __str__(self):
        return f'{self.id} {self.nombre} {self.tipo} '
