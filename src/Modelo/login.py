from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base


class Login(Base):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    usuario = Column(String)
    url = Column(String)
    nota = Column(String)
    clave = Column(String)
    claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'))
