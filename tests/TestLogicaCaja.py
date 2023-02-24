import unittest
from src.logica.LogicaCaja import LogicaCaja

class TestLogicaCaja(unittest.TestCase):

    def test_validar_clave_maestra(self):
        clave=LogicaCaja.validar_clave_maestra(self,'clave')
        self.assertEqual(clave,True)
