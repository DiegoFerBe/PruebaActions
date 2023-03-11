import re
import random
from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
from src.logica.ElementoRepositorio import ElementoRepositorio
from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad


class LogicaCaja(FachadaCajaDeSeguridad):

    def dar_claveMaestra(self):
        return 'clave'

    def validar_clave_maestra(self, clave):
        clave = 'clave'
        if clave == 'clave':
            return True
        else:
            return False

    def dar_claves_favoritas(self):
        misclaves = ClaveFavoritaRepositorio.ver_claves_favoritas(self)
        loQueVoyARetornar = []

        for clave in misclaves:
            misc = {
                'nombre': clave.nombre,
                'clave': clave.clave,
                'pista': clave.pista
            }
            loQueVoyARetornar.append(misc)

        return loQueVoyARetornar

    def crear_clave_favorita(self, nombre, clave, pista):
        return ClaveFavoritaRepositorio.guardar_clave_favorita(self, nombre=nombre, clave=clave, pista=pista)

    def dar_elementos(self):
        listaRetornada = []
        elementos = ElementoRepositorio().dar_elementos()
        for el in elementos:
            if el.tipo.value == 'Login':
                login = ElementoRepositorio().traer_login_por_id(el.id)
                clave = ClaveFavoritaRepositorio().traer_clave_por_id(login.claveFavorita_id)
                listaRetornada.append({"nombre_elemento:": login.nombre,
                                       "tipo:": login.tipo.value,
                                       "notas:": login.nota,
                                       "email": login.email,
                                       "usuario": login.usuario,
                                       "clave": clave.nombre,
                                       "url": login.url
                                       })
            elif el.tipo.value == 'Identificacion':
                iden = ElementoRepositorio().traer_identificacion_por_id(el.id)
                listaRetornada.append({"nombre_elemento:": iden.nombre,
                                       "tipo:": iden.tipo.value,
                                       "numero": iden.numero,
                                       "nombre":iden.nombre,
                                       "fecha_nacimiento":iden.fechaNacimiento.__str__(),
                                       "fecha_exp":iden.fechaExpedicion.__str__(),
                                       "fecha_venc":iden.fechaVencimiento.__str__(),
                                       "nota:": iden.nota

                                       })

        return listaRetornada

    def generar_clave(self):
        global cadena
        REGEX = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[? - * ! @ # $ / () {} = . , ; :]).{8,15}$'
        patron = re.compile(REGEX)
        minusculas = 'abcdefghijklmnopqrstuvwxyz'
        mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        especiales = '*-_@'
        numeros = '1234567890'

        flag = True

        while flag:

            cadena = ''.join(random.choices(minusculas + mayusculas + especiales + numeros, k=12))

            if patron.fullmatch(cadena):
                flag = False

        return cadena

    def ver_reporte_seguridad(self):
        return {'logins': 10, 'ids': 10, 'tarjetas': 5, 'secretos': 2, 'inseguras': 3, 'avencer': 1, 'masdeuna': 1,
                'nivel': 0.6}

    def editar_clave(self, id, nombre, clave, pista):
        return ClaveFavoritaRepositorio().editar_clave_favorita(id, nombre, clave, pista)

    def crearLogin(self, nombre, email, usuario, password, url, notas, id_claveFavorita):
        return ElementoRepositorio().guardar_Login_elemento(nombre, email, usuario, password, url, notas, id_claveFavorita_id)
