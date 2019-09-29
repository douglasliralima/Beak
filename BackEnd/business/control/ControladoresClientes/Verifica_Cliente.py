import os
import sys
import re

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    origin_path = "../../.."
elif _platform == "win32" or "win64":
    # Windows
    origin_path = "..\..\.."
#elif _platform == "darwin":
    # MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

#Funções chamadas em Login
from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha
from database.GerenciadorBancoShelve import GerenciadorBancoShelve

#Objeto Verifica Cliente
class Verifica_Cliente(object):
	def __init__(self, email, senha):
		self.__email = email
		self.__senha = senha
		self.__cliente_valido = False

		self.__gerenciador = GerenciadorBancoShelve()

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
		print('self.__email:', self.__email)
		try:
			self.__cliente_valido = self.__gerenciador.validaCliente(self.__email, self.__senha)
		except Exception as error:
			print('\n', error)

	#def valida_cpf(self):
	#	if re.match(r'[a-zA-Z0-9]{2}-[a-zA-Z0-9]{3}$', inp):
	#		return True
	#	return False'''

	def email_cliente(self):
		return self.__email

	def senha_cliente(self):
		return self.__senha

	def status_cliente(self):
		return self.__cliente_valido
