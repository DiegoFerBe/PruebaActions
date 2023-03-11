from sqlalchemy.exc import SQLAlchemyError

from src.modelo.declarative_base import Base, engine, session
from src.modelo.elemento import Elemento, Tipo
from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
from src.modelo.identificacion import Identificacion
from src.modelo.login import Login
from datetime import datetime

from src.modelo.secreto import Secreto
from src.modelo.tarjeta import Tarjeta


class ElementoRepositorio:

    def __init__(self):
        Base.metadata.create_all(engine)

    def dar_elementos(self):
        return session.query(Elemento).all()

    def dar_login_elementos(self):
        return session.query(Login).all()

    def dar_secreto_elementos(self):
        return session.query(Secreto).all()

    def dar_identificacion_elementos(self):
        return session.query(Identificacion).all()

    def dar_tarjeta_elementos(self):
        return session.query(Tarjeta).all()

    def traer_login_por_id(self, id):
        elementoTraido = session.query(Login).filter_by(id=id).first()
        return elementoTraido

    def traer_identificacion_por_id(self, id):
        elementoTraido = session.query(Identificacion).filter_by(id=id).first()
        return elementoTraido

    def traer_secreto_por_id(self, id):
        elementoTraido = session.query(Secreto).filter_by(id=id).first()
        return elementoTraido

    def traer_tarjeta_por_id(self, id):
        elementoTraido = session.query(Tarjeta).filter_by(id=id).first()
        return elementoTraido

    def traer_elemento_por_id(self, id):
        elementoTraido = session.query(Elemento).get(id).__dict__
        return elementoTraido

    def guardar_Login_elemento(self,nombre,nota, email, usuario, url, clave, claveFavorita):
        try:
            claveRepositorio = ClaveFavoritaRepositorio()
            claveTraida = claveRepositorio.traer_clave_por_id(claveFavorita)

            login = Login(nombre=nombre,tipo=Tipo.LOGIN,nota=nota, email=email, usuario=usuario, url=url, clave=clave,
                      claveFavorita_id=claveTraida.id)
            session.add(login)
            session.commit()
            session.close()
            return True
        except SQLAlchemyError:
            return False

    def guardar_identificacion_elemento(self,nombre,nota, numero, nombreCompleto, fechaNacimiento, fechaExpedicion, fechaVencimiento,telefono):
        fechaNacimiento=datetime.strptime(fechaNacimiento, '%Y-%m-%d').date()
        fechaExpedicion=datetime.strptime(fechaExpedicion, '%Y-%m-%d').date()
        fechaVencimiento=datetime.strptime(fechaVencimiento, '%Y-%m-%d').date()

        identificacion = Identificacion(nombre=nombre,tipo=Tipo.ID,nota=nota,numero=numero,nombreCompleto=nombreCompleto,fechaNacimiento=fechaNacimiento,
                                        fechaExpedicion=fechaExpedicion,fechaVencimiento=fechaVencimiento,telefono=telefono)

        session.add(identificacion)
        session.commit()
        session.close()

    def guardar_tarjeta_elemento(self,nombre,nota,numero,titular,clave,fechaVencimiento,cvv,direccion,telefono,clavefavorita):
        try:
            claveRepositorio = ClaveFavoritaRepositorio()
            claveTraida = claveRepositorio.traer_clave_por_id(clavefavorita)
            tarjeta = Secreto(nombre=nombre,tipo=Tipo.TARJETA,nota=nota,numero=numero,titular=titular,clave=clave,fechaVencimiento=fechaVencimiento,
                              cvv=cvv,direccion=direccion,telefono=telefono,claveFavorita_id=claveTraida.id)
            session.add(tarjeta)
            session.commit()
            session.close()
            return True
        except SQLAlchemyError:
            return False

    def guardar_secreto_elemento(self,nombre,nota,secreto,clavefavorita):
        try:
            claveRepositorio = ClaveFavoritaRepositorio()
            claveTraida = claveRepositorio.traer_clave_por_id(clavefavorita)
            secreto = Secreto(nombre=nombre,tipo=Tipo.SECRETO,nota=nota,secreto=secreto,claveFavorita_id=claveTraida.id)
            session.add(secreto)
            session.commit()
            session.close()
            return True
        except SQLAlchemyError:
            return False

    def eliminar_elemento(self,id_elemento):
        elemento=session.query(Elemento).get(id_elemento)
        if elemento.tipo.value =='Login':
            elemento_borrar=session.query(Login).get(id_elemento)
        elif elemento.tipo.value =='Identificacion':
            elemento_borrar = session.query(Identificacion).get(id_elemento)
        elif elemento.tipo.value =='Secreto':
            elemento_borrar = session.query(Secreto).get(id_elemento)
        elif elemento.tipo.value =='Tarjeta':
            elemento_borrar = session.query(Tarjeta).get(id_elemento)
        session.delete(elemento_borrar)
        session.commit()
        session.close()
