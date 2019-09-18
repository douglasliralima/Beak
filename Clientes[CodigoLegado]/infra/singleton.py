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

class Singleton(object):

    __instance = None

    def __new__(cls, nome):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
            Singleton.__instance.__nome = nome

        return Singleton.__instance

    @property
    def nome(self):
        return self.__nome
