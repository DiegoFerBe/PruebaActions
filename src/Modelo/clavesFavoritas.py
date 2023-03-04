from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.Modelo.login import Login

from .declarative_base import Base


class ClavesFavoritas(Base):
    __tablename__ = 'clavesFavoritas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    clave = Column(String)
    # confirmacionClave = Column(String)
    pista = Column(String)

    logins = relationship('Login', cascade='all')

    def __str__(self):
        return f'{self.id} {self.nombre} {self.clave}'
