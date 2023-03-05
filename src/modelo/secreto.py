from sqlalchemy import Column, Integer, String
from elemento import Elemento
from declarative_base import Base

class Secreto(Base):

  secreto = Column(String)
  claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'))
