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


from business.gerenciadoresRelatorio.relatorioJson import relatorio_json
from business.gerenciadoresRelatorio.relatorioHtml import relatorio_html


class relatorio:
	def __init__(self, tipo):

		tipo = tipo.lower()

		if (tipo == 'json'):
			self.__relatorio = relatorio_json()
		elif (tipo == 'html'):
			self.__relatorio = relatorio_html()

	def getRelatorio(self, dados):
		self.__relatorio.print_relatorio(dados)
