from src.modelo.declarative_base import Base, engine, session
from src.modelo.elemento import Elemento, Tipo
from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
from src.modelo.login import Login


class ElementoRepositorio:

    def __init__(self):
        Base.metadata.create_all(engine)

    def guardar_Elemento(self, nombre, tipo, nota, id_clave):
        e = Elemento(nombre=nombre, tipo=Tipo.LOGIN, nota=nota)

        session.add(e)
        session.commit()
        session.close()

    def traer_elemento_por_id(self, id):
        elementoTraido = session.query(Elemento).get(id).__dict__
        return elementoTraido

    def guardar_Login_elemento(self, email, usuario, url, clave, claveFavorita):
        claveRepo = ClaveFavoritaRepositorio()
        claveTraida = claveRepo.traer_clave_por_id(claveFavorita)

        login = Login(nombre="probando",tipo=Tipo.LOGIN,nota="1234", email=email, usuario=usuario, url=url, clave=clave,
                      claveFavorita_id=claveTraida)

        session.add(Login)
        session.commit()
        session.close()
