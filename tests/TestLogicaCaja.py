import unittest
from src.logica.LogicaCaja import LogicaCaja


class TestLogicaCaja(unittest.TestCase):

    def test_validar_clave_maestra(self):
        clave = LogicaCaja.validar_clave_maestra(self, 'clave')
        self.assertEqual(clave, True)

    def test_ver_claves_favoritas(self):
        clavesFavortias = LogicaCaja.ver_claves_favoritas(self)
        self.assertEqual(clavesFavortias, [])

    def test_crear_clave_favorita(self):
        crearClaveFavorita = LogicaCaja.crear_clave_favorita(self, 'prueba','erferfre','erferfre','la pista')
        self.assertEqual(crearClaveFavorita, True)

    def test_ver_elementos(self):
        elementos = LogicaCaja.ver_elementos(self)
        self.assertEqual(elementos, [])

    def test_generar_clave(self):
        claveGenerada = LogicaCaja.generar_clave(self)
        self.assertRegex(claveGenerada,r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[? - * ! @ # $ / () {} = . , '
                                       r'; :]).{8,15}$')
