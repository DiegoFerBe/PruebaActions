from sqlalchemy import Column, Integer, String
from .elemento import Elemento

class ElementoConClave(Elemento):

  clave = Column(String)
