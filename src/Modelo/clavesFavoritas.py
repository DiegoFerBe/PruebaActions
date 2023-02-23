from sqlalchemy import Column, Integer, String
from .declarative_base import Base

from sqlalchemy.orm import relationship

class ClavesFavoritas(Base):

  __tablename__ = 'clavesFavoritas'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)
  clave = Column(String)
  confirmacionClave = Column(String)
  pista = Column(String)
  elementoTiene = relationship('Elemento Con Clave', cascade='all')
