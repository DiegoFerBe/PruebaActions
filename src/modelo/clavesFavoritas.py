from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.modelo.login import Login
from src.modelo.secreto import Secreto
from src.modelo.tarjeta import Tarjeta

from .declarative_base import Base


class ClavesFavoritas(Base):
    __tablename__ = 'clavesFavoritas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    clave = Column(String)
    pista = Column(String)

    logins = relationship('Login', backref="clavesFavoritas")
    #secretos = relationship('Secreto', cascade='all')
    #tarjetas = relationship('Tarjeta', cascade='all')

    def __str__(self):
        return f'{self.id} {self.nombre} {self.clave}'
