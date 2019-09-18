#Fila de Execução dos comandos
class Fila_de_trabalho(object):
	def __init__(self):
		self.__comandos = []

	def adiciona(self, comando):
		self.__comandos.append(comando)

	def processa(self):
		for comando in self.__comandos:
			comando.executa()
