import re
import random
from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
from src.logica.ElementoRepositorio import ElementoRepositorio
from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad
from datetime import date


class LogicaCaja(FachadaCajaDeSeguridad):

    def __init__(self):
        self.clave_maestra = 'clave'

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

    def dar_clave_favorita(self, id_clave):
        clave = ClaveFavoritaRepositorio().traer_clave_por_id(id_clave)
        if clave is not None:
            return {'nombre': clave.nombre, 'clave': clave.clave, 'pista': clave.pista}

    def crear_clave_favorita(self, nombre, clave, pista):
        return ClaveFavoritaRepositorio().guardar_clave_favorita(nombre, clave, pista)

    def dar_elementos(self):
        listaRetornada = []
        elementos = ElementoRepositorio().dar_elementos()
        for el in elementos:
            if el.tipo.value == 'Login':
                login = ElementoRepositorio().traer_login_por_id(el.id)
                clave = ClaveFavoritaRepositorio().traer_clave_por_id(login.claveFavorita_id)
                listaRetornada.append({"nombre_elemento:": login.nombre,
                                       "tipo:": login.tipo.value,
                                       "email": login.email,
                                       "usuario": login.usuario,
                                       "clave": clave.nombre,
                                       "url": login.url,
                                       "notas:": login.nota
                                       })
            elif el.tipo.value == 'Identificacion':
                iden = ElementoRepositorio().traer_identificacion_por_id(el.id)
                listaRetornada.append({"nombre_elemento:": iden.nombre,
                                       "tipo:": iden.tipo.value,
                                       "numero": iden.numero,
                                       "nombre": iden.nombre,
                                       "fecha_nacimiento": iden.fechaNacimiento.__str__(),
                                       "fecha_exp": iden.fechaExpedicion.__str__(),
                                       "fecha_venc": iden.fechaVencimiento.__str__(),
                                       "notas:": iden.nota

                                       })
            elif el.tipo.value == 'Secreto':
                secret = ElementoRepositorio().traer_secreto_por_id(el.id)
                clave = ClaveFavoritaRepositorio().traer_clave_por_id(secret.claveFavorita_id)
                listaRetornada.append({"nombre_elemento:": secret.nombre,
                                       "tipo:": secret.tipo.value,
                                       "secreto": secret.secreto,
                                       "clave": clave.nombre,
                                       "notas:": secret.nota

                                       })

            elif el.tipo.value == 'Tarjeta':
                tarjeta = ElementoRepositorio().traer_tarjeta_por_id(el.id)
                clave = ClaveFavoritaRepositorio().traer_clave_por_id(tarjeta.claveFavorita_id)
                listaRetornada.append({"nombre_elemento:": tarjeta.nombre,
                                       "tipo:": tarjeta.tipo.value,
                                       "numero": tarjeta.numero,
                                       "titular": tarjeta.titular,
                                       "fecha_venc": tarjeta.fechaVencimiento,
                                       "ccv": tarjeta.cvv,
                                       "clave": clave.nombre,
                                       "direccion":tarjeta.direccion,
                                       "telefono":tarjeta.telefono,
                                       "notas:": tarjeta.nota

                                       })

        return listaRetornada

    def dar_elemento(self, id_elemento):
        elemento = ElementoRepositorio().traer_elemento_por_id(id_elemento)
        if elemento.tipo.value == 'Login':
            return ElementoRepositorio().traer_login_por_id(elemento.id)
        elif elemento.tipo.value == 'Secreto':
            return ElementoRepositorio().traer_secreto_por_id(elemento.id)
        elif elemento.tipo.value == 'Tarjeta':
            return ElementoRepositorio().traer_tarjeta_por_id(elemento.id)
        elif elemento.tipo.value == 'Identificacion':
            return ElementoRepositorio().traer_identificacion_por_id(elemento.id)

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

    def editar_clave(self, id, nombre, clave, pista):
        return ClaveFavoritaRepositorio().editar_clave_favorita(id, nombre, clave, pista)

    def crearLogin(self, nombre, email, usuario, password, url, notas, id_claveFavorita):
        return ElementoRepositorio().guardar_Login_elemento(nombre, email, usuario, password, url, notas, id_claveFavorita)

    def ver_reporte_seguridad(self):

        cantLogins = len(ElementoRepositorio().dar_login_elementos())
        cantTarjetas = len(ElementoRepositorio().dar_tarjeta_elementos())
        cantSecretos = len(ElementoRepositorio().dar_secreto_elementos())
        cantIdentificaciones = len(ElementoRepositorio().dar_identificacion_elementos())
        cantClaves = len(ClaveFavoritaRepositorio().ver_claves_favoritas())
        inseguras = 0
        avencer = 0
        masdeuna = 0
        masdetres = False
        fechaActual = date.today()

        clavesFavoritas = ClaveFavoritaRepositorio().ver_claves_favoritas()

        REGEX = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[? - * ! @ # $ / () {} = . , ; :]).{8,15}$'
        patron = re.compile(REGEX)

        for clave in clavesFavoritas:
            if not patron.fullmatch(clave.clave):
                inseguras += 1

        identificaciones = ElementoRepositorio().dar_identificacion_elementos()
        tarjetas = ElementoRepositorio().dar_tarjeta_elementos()
        logins = ElementoRepositorio().dar_login_elementos()
        secretos = ElementoRepositorio().dar_secreto_elementos()

        historialClaves = []

        for identificacion in identificaciones:
            if (identificacion.fechaVencimiento - fechaActual).days < 90:
                avencer += 1

        for tarjeta in tarjetas:
            historialClaves.append(tarjeta.claveFavorita_id)
            if (tarjeta.fechaVencimiento - fechaActual).days < 90:
                avencer += 1

        for secreto in secretos:
            historialClaves.append(secreto.claveFavorita_id)

        for login in logins:
            historialClaves.append(login.claveFavorita_id)

        clavesUsadas = set(historialClaves)

        for usadas in clavesUsadas:
            contador = 0
            for historial in historialClaves:
                if usadas == historial:
                    contador += 1
                    if contador == 2:
                        masdeuna += 1
                    elif contador > 3:
                        masdetres = True
                        break

        if (cantClaves == 0):
            SC = 0
        else:
            SC = ((cantClaves - inseguras) / cantClaves) * 100

        if (cantIdentificaciones + cantTarjetas == 0):
            V = 0
        else:
            V = ((cantIdentificaciones + cantTarjetas - avencer) / cantIdentificaciones + cantTarjetas) * 100

        R = 100

        if masdetres:
            R = 0
        elif masdeuna > 0:
            R = 50

        nivel = SC * 0.5 + V * 0.2 + R * 0.3

        return {'logins': cantLogins, 'ids': cantIdentificaciones, 'tarjetas': cantTarjetas, 'secretos': cantSecretos,
                'inseguras': inseguras, 'avencer': avencer, 'masdeuna': masdeuna, 'nivel': nivel}






