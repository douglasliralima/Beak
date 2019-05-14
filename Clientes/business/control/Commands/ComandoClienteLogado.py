from business.control.Commands.Comando import Comando

#Comandos para salvar usuário logado
class comando_cliente_logado(Comando):
	def __init__(self, clientes_logados):
		self.__login = clientes_logados

	def executa(self):
		self.__login.add_cliente_logado()