from src.modelo.declarative_base import Base, engine, session
from src.modelo.elemento import Elemento, Tipo
from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
from src.modelo.identificacion import Identificacion
from src.modelo.login import Login
from datetime import datetime

from src.modelo.secreto import Secreto


class ElementoRepositorio:

    def __init__(self):
        Base.metadata.create_all(engine)

    def dar_elementos(self):
        return session.query(Elemento).all()

    def traer_elemento_por_id(self, id):
        elementoTraido = session.query(Elemento).get(id).__dict__
        return elementoTraido

    def guardar_Login_elemento(self,nombre,nota, email, usuario, url, clave, claveFavorita):
        claveRepositorio = ClaveFavoritaRepositorio()
        claveTraida = claveRepositorio.traer_clave_por_id(claveFavorita)

        login = Login(nombre=nombre,tipo=Tipo.LOGIN,nota=nota, email=email, usuario=usuario, url=url, clave=clave,
                      claveFavorita_id=claveTraida)

        session.add(login)
        session.commit()
        session.close()

    def guardar_identificacion_elemento(self,nombre,nota, numero, nombreCompleto, fechaNacimiento, fechaExpedicion, fechaVencimiento,telefono):
        fechaNacimiento=datetime.strptime(fechaNacimiento, '%Y-%m-%d').date()
        fechaExpedicion=datetime.strptime(fechaExpedicion, '%Y-%m-%d').date()
        fechaVencimiento=datetime.strptime(fechaVencimiento, '%Y-%m-%d').date()

        identificacion = Identificacion(nombre=nombre,tipo=Tipo.ID,nota=nota,numero=numero,nombreCompleto=nombreCompleto,fechaNacimiento=fechaNacimiento,
                                        fechaExpedicion=fechaExpedicion,fechaVencimiento=fechaVencimiento,telefono=telefono)

        session.add(identificacion)
        session.commit()
        session.close()

    def guardar_secreto_elemento(self,nombre,nota,secreto,clavefavorita):
        secreto = Secreto(nombre=nombre,nota=nota,secreto=secreto,claveFavorita_id=clavefavorita)

        session.add(secreto)
        session.commit()
        session.close()

