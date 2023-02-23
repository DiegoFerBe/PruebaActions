from sqlalchemy import Column, Integer, String
from .elementoconclave import ElementoConClave

class Tarjeta(ElementoConClave):

  numero = Column(Int)
  titular = Column(String)
  fechaVencimiento = Column(Date)
  cvv = Column(Int)
  direccion = Column(String)
  telefono = Column(String)
  nota = Column(String)
