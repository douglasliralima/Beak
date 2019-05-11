from abc import ABC, abstractmethod

class Adaptador(ABC):
    
    @abstractmethod
    def operacao(self):
        pass