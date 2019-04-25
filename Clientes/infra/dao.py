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

from infra.gerenciadores.shelveDB.GerenciadorBancoShelve import GerenciadorBancoShelve
from infra.gerenciadores.pickleDB.GerenciadorBancoPickle import GerenciadorBancoPickle

class factory:
    def __init__(self, banco):
        if (banco == 'shelve'):
            self.__gerenciador = GerenciadorBancoShelve()
        elif (banco == 'pickle'):
            self.__gerenciador = GerenciadorBancoPickle()

    def banco(self):
        return self.__gerenciador


def getBanco(banco):
    return factory(banco).banco()
