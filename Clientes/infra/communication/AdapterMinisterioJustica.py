import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	# linux
	origin_path = "../.."
elif _platform == "win32" or "win64":
	# Windows
	origin_path = "../.."
#elif _platform == "darwin":
	# MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

from infra.communication.Adapter import Adaptador
from mocks.mockMinisterioJustica import MinisterioJustica
#asd
class AdapterReceitaFederal(Adaptador):
    @staticmethod
    def operacao(rg, cpf):
        MinisterioJustica.AntecedenteCriminal(rg, cpf)