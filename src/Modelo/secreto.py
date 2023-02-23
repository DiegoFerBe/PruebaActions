from sqlalchemy import Column, Integer, String
from elementoConClave import ElementoConClave

class Secreto(ElementoConClave):

  secreto = Column(String)
  nota = Column(String)
