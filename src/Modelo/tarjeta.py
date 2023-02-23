from sqlalchemy import Column, Integer, String, Date
from elementoConClave import ElementoConClave

class Tarjeta(ElementoConClave):

  numero = Column(Integer)
  titular = Column(String)
  fechaVencimiento = Column(Date)
  cvv = Column(Integer)
  direccion = Column(String)
  telefono = Column(String)
  nota = Column(String)
