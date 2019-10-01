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

    def persisteServico(self, servico):
        self.__db[servico.getId()] = servico
        return True

    def getServico(self, ident):
        return self.__db[ident]

    def excluiServico(self, ident):
        del self.__db[ident]
        return True

    def validaServico(self, ident):
        if ident in list(self.__db.keys()):
            return False
            raise EmailExistenteException

        return True

    def isPendente(self, ident):
        if self.__db[ident].getStatus() == "pendente":
            return True
        else:
            return False

    def isAndamento(self, ident):
        if self.__db[ident].getStatus() == "andamento":
            return True
        else:
            return False

    def isFinalizado(self, indet):
        if self.__db[ident].getStatus() == "finalizado":
            return True
        else:
            return False

    def retornaStatus(self, ident):
        return self.__db[ident].getStatus()

    def closeDB(self):
        self.__db.close()
