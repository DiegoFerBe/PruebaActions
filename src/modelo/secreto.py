from sqlalchemy import Column, Integer, String, ForeignKey
from src.modelo.elemento import Elemento


class Secreto(Elemento):

    __tablename__ = 'secretos'

    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)
    secreto = Column(String)
    claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'),nullable=False)
