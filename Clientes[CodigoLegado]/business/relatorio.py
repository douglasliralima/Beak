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
