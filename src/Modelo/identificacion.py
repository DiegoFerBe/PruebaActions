from sqlalchemy import Column, Integer, String, Date
from elementoSinClave import ElementoSinClave


class Identificacion(ElementoSinClave):
  numero = Column(Integer)
  nombreCompleto = Column(String)
  fechaNacimiento = Column(Date)
  fechaExpedicion = Column(Date)
  fechaVencimiento = Column(Date)
  telefono = Column(String)
  nota = Column(String)