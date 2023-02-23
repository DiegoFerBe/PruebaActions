from sqlalchemy import Column, Integer, String, ForeignKey
from .elemento import Elemento

class ElementoConClave(Elemento):

  clave = Column(String)
  clavesFavoritas = Column(String, ForeignKey('clavesFavoritas.id'))
