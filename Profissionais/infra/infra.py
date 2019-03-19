import os
import sys

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    origin_path = ".."
elif _platform == "win32" or "win64":
    # Windows
    origin_path = ".."
#elif _platform == "darwin":
    # MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

from business.control.Exceptions.ClienteInexistenteException import ClienteInexistenteException
from business.control.Exceptions.EmailExistenteException import EmailExistenteException
import shelve

from business.model.cliente import Cliente


class GerenciadorBanco:
    def __init__(self):
        #if _platform == "linux" or _platform == "linux2":
            # linux
         #   filename = "infra/clientes.db"
        #elif _platform == "win32" or "win64":
            #windows
         #   filename = 'infra\clientes.db'
         filename = os.path.dirname(os.path.abspath(__file__)) + "/clientes.db"
         self.__db = shelve.open(filename, flag='c')

    def validaCliente(self, email, senha):

        if (email in list(self.__db.keys())) and (self.__db[email].getSenha() == senha):
            return True
        else:
            raise ClienteInexistenteException

    def persisteCliente(self, cliente):
        self.__db[cliente.getEmail()] = cliente
        return True

    def getCliente(self, email):
        return self.__db[email]

    def excluiCliente(self, email):
        del self.__db[email]
        return True

    def validaEmail(self, email):
        if email in list(self.__db.keys()):
            raise EmailExistenteException
        return True

    def closeDB(self):
        self.__db.close()
