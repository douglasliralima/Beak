import sys
from sys import platform as _platform
import threading
from datetime import datetime

if _platform == "linux" or _platform == "linux2":
	# linux
	origin_path = "/.."
elif _platform == "win32" or "win64":
	# Windows
	origin_path = ".."
#elif _platform == "darwin":
	# MAC OS X

if origin_path not in sys.path:
	sys.path.append(origin_path)


#Importando biblioteca para o Command
from abc import ABC, abstractmethod, ABCMeta

#Classes de controle
from business.control.ControladoresClientes.Verifica_Cliente import Verifica_Cliente
from business.control.ControladoresClientes.Builder_Cliente import Builder_Cliente

class FacadeGerenciamentoUsuario:

	#Função do FacadeGerenciamentoUsuario que verifica se o cliente existe no banco
	#Também valida o email e a senha antes de verificar se o cliente existe
	@staticmethod
	def valida_cliente(email, senha):

		cliente_login = Verifica_Cliente(email, senha).valida_cliente()
		print('cliente_login:', cliente_login)

		result = Verifica_Cliente.status_cliente
		print('result:', result)
		return result

	#Função que adiciona cliente no banco
	@staticmethod
	def add_cliente(nome, senha, email, dataNasc, cpf, foto, telefone, endereco):
		cliente_cadastro = Builder_Cliente(nome, senha, email, dataNasc, cpf, foto, telefone, endereco)
