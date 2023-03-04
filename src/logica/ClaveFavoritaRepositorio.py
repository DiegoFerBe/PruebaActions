from sqlalchemy.exc import SQLAlchemyError
from src.Modelo.declarative_base import engine, Base, session
from src.Modelo.clavesFavoritas import ClavesFavoritas


class ClaveFavoritaRepositorio:

    def __init__(self):
        Base.metadata.create_all(engine)

    def guardar_clave_favorita(self,nombre, clave, pista):
        try:
            c = ClavesFavoritas(nombre=nombre, clave=clave, pista=pista)
            session.add(c)
            session.commit()
            session.close()
            return True
        except SQLAlchemyError:
            return False

    def ver_claves_favoritas(self):
        clavesFavoritas = session.query(ClavesFavoritas).all()
        session.close()
        return clavesFavoritas
