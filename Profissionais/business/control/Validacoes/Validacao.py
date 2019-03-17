from abc import ABC, abstractmethod

class Validacao(ABC):
    
    @abstractmethod
    def valida(self, entrada):
        pass