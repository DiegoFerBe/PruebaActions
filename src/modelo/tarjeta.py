from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.modelo.elemento import Elemento


class Tarjeta(Elemento):
    __tablename__ = 'tarjetas'

    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)

    numero = Column(Integer)
    titular = Column(String)
    fechaVencimiento = Column(Date)
    cvv = Column(Integer)
    direccion = Column(String)
    telefono = Column(String)
    claveFavorita_id = Column(Integer, ForeignKey('clavesFavoritas.id'),nullable=False)
