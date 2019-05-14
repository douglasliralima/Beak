from business.control.Commands.Comando import Comando

class comando_verifica_cliente(Comando):

	def __init__(self, verifica_cliente):
		self.__cliente_validado = verifica_cliente

	def executa(self):
		self.__cliente_validado.valida_cliente