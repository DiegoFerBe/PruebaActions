from sqlalchemy import Column, Integer, String
from .elementoconclave import ElementoConClave

class Secreto(ElementoConClave):

  secreto = Column(String)
  nota = Column(String)
