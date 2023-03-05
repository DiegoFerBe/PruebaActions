from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modelo.elemento import Elemento


class Login(Elemento):

    __tablename__ = 'logins'

    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)
    email = Column(String)
    usuario = Column(String)
    url = Column(String)
    clave = Column(String)
    claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'))
    #elemento = relationship('Elemento', uselist=False)

    def __str__(self):
        return f'{self.id} {self.nombre} {self.clave} {self.tipo} {self.usuario}'

