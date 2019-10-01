import os
import sys

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    origin_path = "../../.."
elif _platform == "win32" or "win64":
    # Windows
    origin_path = "..\..\.."
#elif _platform == "darwin":
    # MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

#from business.control.Exceptions.ClienteInexistenteException import ClienteInexistenteException
#from business.control.Exceptions.EmailExistenteException import EmailExistenteException
import shelve

from classes.servico import Servico


class servicoBD:
    def __init__(self):
        #if _platform == "linux" or _platform == "linux2":
            # linux
         #   filename = "infra/clientes.db"
        #elif _platform == "win32" or "win64":
            #windows
         #   filename = 'infra\clientes.db'
         filename = os.path.dirname(os.path.abspath(__file__)) + "/servicos.db"
         #filename = 'clientes.db'
         self.__db = shelve.open(filename, flag='c')

    #def validaServico(self, id):
    #    if (email in list(self.__db.keys())) and (self.__db[email].getSenha() == senha):
    #        return True
    #    else:
    #        return False
            #raise ClienteInexistenteException

    def persisteServico(self, servico):
        self.__db[servico.getId()] = servico
        return True

    def getServico(self, ident):
        return self.__db[ident]

    def excluiCliente(self, ident):
        del self.__db[ident]
        return True

    def validaServico(self, ident):
        if ident in list(self.__db.keys()):
            return False
            raise EmailExistenteException

        return True


    def closeDB(self):
        self.__db.close()