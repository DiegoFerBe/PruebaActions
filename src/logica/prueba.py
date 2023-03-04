from src.logica.ClaveFavoritaRepositorio import ClaveFavoritaRepositorio
from src.logica.LogicaCaja import LogicaCaja

claveMethod = ClaveFavoritaRepositorio()
logicaCaja = LogicaCaja()

print(claveMethod.guardar_clave_favorita("diego","diego","algo"))


