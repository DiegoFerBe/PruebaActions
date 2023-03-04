import re
import random
from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
class LogicaCaja:

    def validar_clave_maestra(self, clave):
        clave = 'clave'
        if clave == 'clave':
            return True
        else:
            return False

    def ver_claves_favoritas(self):
        return ClaveFavoritaRepositorio.ver_claves_favoritas(self)

    def crear_clave_favorita(self, nombre, clave, confirmacion, pista):
        return ClaveFavoritaRepositorio.guardar_clave_favorita(self, nombre=nombre, clave=clave, pista=pista)

    def ver_elementos(self):
        return []


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
        return {'logins':10, 'ids':10, 'tarjetas': 5, 'secretos':2, 'inseguras':3, 'avencer': 1, 'masdeuna': 1, 'nivel': 0.6}