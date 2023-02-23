from sqlalchemy import Column, Integer, String
from elementoConClave import ElementoConClave

class Login(ElementoConClave):

  email = Column(String)
  usuario = Column(String)
  url = Column(String)
  nota = Column(String)
