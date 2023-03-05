from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.modelo.elemento import Elemento


class Identificacion(Elemento):

    __tablename__ = 'identificaciones'

    id = Column(Integer, ForeignKey('elementos.id'), primary_key=True)
    numero = Column(Integer)
    nombreCompleto = Column(String)
    fechaNacimiento = Column(Date)
    fechaExpedicion = Column(Date)
    fechaVencimiento = Column(Date)
    telefono = Column(String)
