from infra.usuariosLogados import saveLoggedClients

class Clientes_Logados(object):
	def __init__(self, email):
		self.__email = email

	def add_cliente_logado(self):
		try:
			saveLoggedClients(self.__email)
		except Exception as error:
			print('\n', error)