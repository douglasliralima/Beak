from abc import ABC, abstractmethod, ABCMeta

#Interface do Comando
class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass
