import unittest
from faker import Faker
import random

from src.logica.LogicaCaja import LogicaCaja
from src.modelo.declarative_base import Session, Base, engine
from src.modelo.clavesFavoritas import ClavesFavoritas


class TestLogicaCaja(unittest.TestCase):

    def setUp(self):

        self.Base = Base

        self.Base.metadata.create_all(engine)

        self.logicCaja = LogicaCaja()

        self.session = Session()

        self.data_factory = Faker()

        self.initClaveFavorita = ClavesFavoritas(nombre=self.data_factory.name(),clave=self.data_factory.password(),pista=self.data_factory.text())

        self.session.add(self.initClaveFavorita)

        self.session.commit()

    def test_validar_clave_maestra(self):
        clave = LogicaCaja.validar_clave_maestra(self, 'clave')
        self.assertEqual(clave, True)

    def test_ver_claves_favoritas(self):
        claves = LogicaCaja().dar_claves_favoritas()
        self.assertGreaterEqual(claves.__len__(), 0)

    def test_crear_clave_favorita(self):
        nombre = self.data_factory.name()
        clave = self.data_factory.password()
        pista = self.data_factory.text()
        crearClaveFavorita = self.logicCaja.crear_clave_favorita(nombre, clave, pista)
        self.assertEqual(crearClaveFavorita, True)

    def test_ver_elementos(self):
        elementos = LogicaCaja.ver_elementos(self)
        self.assertEqual(elementos, [])

    def test_generar_clave(self):
        claveGenerada = LogicaCaja.generar_clave(self)
        self.assertRegex(claveGenerada, r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[? - * ! @ # $ / () {} = . , '
                                        r'; :]).{8,15}$')

    def test_ver_reporte_seguridad(self):
        logicaCaja = LogicaCaja().ver_reporte_seguridad()
        self.assertEqual(
            {'logins': 10, 'ids': 10, 'tarjetas': 5, 'secretos': 2, 'inseguras': 3, 'avencer': 1, 'masdeuna': 1,
             'nivel': 0.6}, logicaCaja)





    def tearDown(self):

        self.session = Session()

        busqueda = self.session.query(ClavesFavoritas).all()

        for clave in busqueda:
            self.session.delete(clave)

        self.session.commit()
        self.session.close()