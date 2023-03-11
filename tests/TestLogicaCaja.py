import unittest
from faker import Faker
import random

from src.logica.LogicaCaja import LogicaCaja
from src.modelo.declarative_base import Session, Base, engine
from src.modelo.clavesFavoritas import ClavesFavoritas
from src.modelo.identificacion import Identificacion
from src.modelo.login import Login
from src.modelo.secreto import Secreto
from src.modelo.tarjeta import Tarjeta


class TestLogicaCaja(unittest.TestCase):

    def setUp(self):
        self.Base = Base

        self.Base.metadata.create_all(engine)

        self.logicCaja = LogicaCaja()

        self.session = Session()

        self.data_factory = Faker()

        self.initClaveFavorita = ClavesFavoritas(nombre=self.data_factory.name(), clave=self.data_factory.password(),
                                                 pista=self.data_factory.text())

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
        elementos = LogicaCaja().dar_elementos()
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

    def testCrearLogin(self):
        nombre = self.data_factory.word()
        email = self.data_factory.email()
        usuario = self.data_factory.user_name()
        password = self.data_factory.password()
        url = self.data_factory.url()
        notas = self.data_factory.text()

        elemento = self.logicCaja.crearLogin(nombre, email, usuario, password, url, notas,1)

        self.assertTrue(elemento)

    def test_editar_clave(self):
        nuevoNombre = self.data_factory.word()
        nuevaPista = self.data_factory.text()
        nuevaClave = self.data_factory.password()

        respuesta = self.logicCaja.editar_clave(1, nuevoNombre, nuevaClave, nuevaPista)

        self.assertTrue(respuesta, True)

    def tearDown(self):
        self.session = Session()

        busquedaClaves = self.session.query(ClavesFavoritas).all()
        busquedaLogin = self.session.query(Login).all()
        busquedaSecreto = self.session.query(Secreto).all()
        busquedaIdentificacion = self.session.query(Identificacion).all()
        busquedaTarjeta = self.session.query(Tarjeta).all()

        for elemento in busquedaLogin:
            self.session.delete(elemento)

        for elemento in busquedaSecreto:
            self.session.delete(elemento)

        for elemento in busquedaIdentificacion:
            self.session.delete(elemento)

        for elemento in busquedaTarjeta:
            self.session.delete(elemento)

        for clave in busquedaClaves:
            self.session.delete(clave)

        self.session.commit()
        self.session.close()
