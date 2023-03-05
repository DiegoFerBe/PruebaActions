from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import engine, Base, session
from src.modelo.clavesFavoritas import ClavesFavoritas


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

    def traer_clave_por_id(self,id):
        claveTraida = session.query(ClavesFavoritas).get(id).__dict__
        return claveTraida
