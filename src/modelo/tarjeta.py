from sqlalchemy import Column, Integer, String, Date, ForeignKey
from elemento import Elemento
from declarative_base import Base

class Tarjeta(Base):

  numero = Column(Integer)
  titular = Column(String)
  fechaVencimiento = Column(Date)
  cvv = Column(Integer)
  direccion = Column(String)
  telefono = Column(String)
  claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'))
