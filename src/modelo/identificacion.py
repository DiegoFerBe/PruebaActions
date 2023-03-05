from sqlalchemy import Column, Integer, String, Date
from elemento import Elemento
from declarative_base import Base


class Identificacion(Base):
  numero = Column(Integer)
  nombreCompleto = Column(String)
  fechaNacimiento = Column(Date)
  fechaExpedicion = Column(Date)
  fechaVencimiento = Column(Date)
  telefono = Column(String)