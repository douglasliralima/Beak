from business.control.Commands.Comando import Comando

#Comandos do Cadastro
class comando_adiciona_cliente(Comando):
	def __init__(self, adiciona_cliente):
		self.__banco_cliente = adiciona_cliente

	def executa(self):
		self.__banco_cliente.adicionando()
