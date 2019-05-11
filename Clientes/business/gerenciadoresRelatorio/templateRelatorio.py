from abc import ABC, abstractmethod


class templateRelatorio(ABC):

    #template method para geração de relatório
    def print_relatorio(self, dados):
        print(self.geraRelatorio(dados))

    @abstractmethod
    def geraRelatorio(self, dados):
        pass