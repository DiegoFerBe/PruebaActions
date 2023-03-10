from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import engine, Base, session
from src.modelo.clavesFavoritas import ClavesFavoritas


class ClaveFavoritaRepositorio:

    def __init__(self):
        Base.metadata.create_all(engine)

    def guardar_clave_favorita(self, nombre, clave, pista):
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

    def traer_clave_por_id(self, id):
        return session.query(ClavesFavoritas).get(id)

    def editar_clave_favorita(self, id, nombre, clave, pista):
        try:
            claveRecuperada = self.traer_clave_por_id(id)
            if claveRecuperada==None:
                return False
            if len(nombre) > 1:
                claveRecuperada.nombre = nombre
            if len(clave) > 1:
                claveRecuperada.clave = clave
            claveRecuperada.pista = pista

            session.commit()
            session.close()
            return True
        except SQLAlchemyError:
            return False
