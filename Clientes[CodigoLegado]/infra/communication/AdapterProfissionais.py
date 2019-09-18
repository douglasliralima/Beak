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
from mocks.mockProfissional import Profissionais

class AdapterConfirmaProfissionais(Adaptador):

    @staticmethod
    def operacao(idProfissional):
        return Profissionais.confirmaServico(idProfissional)


class AdapterPagamentoProfissionais(Adaptador):

    @staticmethod
    def operacao(IdProfissional, idServico):
        return Profissionais.pagamento(IdProfissional, idServico)


class AdapterAvaliacaoProfissionais(Adaptador):

    @staticmethod
    def operacao(idProfissional, avaliacao):
        return Profissionais.avaliacaoServico(idProfissional, avaliacao)


