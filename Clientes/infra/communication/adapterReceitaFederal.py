import sys

from sys import platform as _platform
from infra.communication.adaptador import Adaptador
from Mocks.mockReceitaFederal import validadorReceitaFederal

class AdapterReceitaFederal(Adaptador):
    def __init__(self):
        self.__receitaFederal = validadorReceitaFederal()
        
    def operador(self, cpf, nascimento):
        self.__receitaFederal.validaCPF(cpf, nascimento)