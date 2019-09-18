
#Funções chamadas em Login
from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha
from business.model.cliente import Cliente
from infra.usuariosLogados import saveLoggedClients
from infra import dao


#Objeto Verifica Cliente
class Verifica_Cliente(object):
	def __init__(self, email, senha):
		self.__email = email
		self.__senha = senha
		self.__cliente_valido = False

		banco = 'shelve'
		self.__gerenciador = dao.getBanco(banco)

	def valida_login(self):
		try:
			self.__email = ValidaFormatoLogin().valida(self.__email.lower())
		except Exception as error:
			print('\n', error)

	def valida_senha(self):
		try:
			self.__senha = ValidaFormatoSenha().valida(self.__senha)
		except Exception as error:
			print('\n', error)

	def valida_cliente(self):

		try:
			self.__cliente_valido = self.__gerenciador.validaCliente(self.__email, self.__senha)
		except Exception as error:
			print('\n', error)

	def email_cliente(self):
		return self.__email

	def senha_cliente(self):
		return self.__senha

	def status_cliente(self):
		return self.__cliente_valido
