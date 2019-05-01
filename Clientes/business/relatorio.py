import sys
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	# linux
	origin_path = "/.."
elif _platform == "win32" or "win64":
	# Windows
	origin_path = ".."
#elif _platform == "darwin":
	# MAC OS X

#print('origin_path:', sys.path)
if origin_path not in sys.path:
	sys.path.append(origin_path)

from business.gerenciadoresRelatorio import relatorioJson, relatorioHtml

class relatorio:
	def __init__(self, tipo, dados):

		tipo = tipo.lower()

		if (tipo == 'json'):
			self.__relatorioDados = relatorioJson.geraRelatorio(dados)
		elif (tipo == 'html'):
			self.__relatorioDados = relatorioHtml.geraRelatorio(dados)

	def relatorio(self):
		return self.__relatorioDados

def getRelatorio(tipo, dados):
	resultadoRelatorio = relatorio(tipo, dados).relatorio()
	print('Relatório:', resultadoRelatorio)
