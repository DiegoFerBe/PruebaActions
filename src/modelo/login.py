from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modelo.elemento import Elemento


class Login(Elemento):

    __tablename__ = 'logins'

    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)
    email = Column(String)
    usuario = Column(String)
    url = Column(String)
    claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'),nullable=False)
    #claveFavorita = relationship('ClavesFavoritas', back_populates='logins')

    def __str__(self):
        return f'email: {self.email}, usuario: {self.usuario},  clave: {self.claveFavorita_id}, url: {self.url}'

