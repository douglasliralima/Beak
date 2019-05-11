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

#Funções de Cadastro
from business.control.addCliente import addCliente

#Funções chamadas em Login
from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha
from business.model.cliente import Cliente
from infra.usuariosLogados import saveLoggedClients
from infra import dao

#Importando biblioteca para o Command
from abc import ABC, abstractmethod, ABCMeta

#classe que gera Relatório
from business.relatorio import relatorio

#Banco que estamos usando
banco = 'shelve'
gerenciador = dao.getBanco(banco)

frequenciaDeAcesso = 0
frequenciaDeAcessoAnterior = 0
tempoPassado = 0
horaPassada = datetime.now()

#Objeto Verifica Cliente
class Verifica_Cliente(object):
	def __init__(self, email, senha):
		self.__email = email
		self.__senha = senha
		self.__cliente_valido = False

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

	#Valida Cliente
	def valida_cliente(self):
		global gerenciador

		try:
			self.__cliente_valido = gerenciador.validaCliente(self.__email, self.__senha)
		except Exception as error:
			print('\n', error)

	@property
	def email_cliente(self):
		return self.__email

	@property
	def senha_cliente(self):
		return self.__senha

	@property
	def status_cliente(self):
		return self.__cliente_valido

class Adiciona_Cliente(object):
	def __init__(self, nome, senha, email, dataNasc, cpf, rg, telefone, endereco):
		self.__nome = nome
		self.__senha = senha
		self.__email = email
		self.__dataNasc = dataNasc
		self.__cpf = cpf
		self.__rg = rg
		self.__telefone = telefone
		self.__endereco = endereco

	def adicionando(self):
		try:
			addCliente(self.__nome, self.__senha, self.__email, self.__dataNasc, self.__cpf, self.__rg, self.__telefone, self.__endereco)
		except Exception as E:
			print(E)

class Clientes_Logados(object):
	def __init__(self, email):
		self.__email = email

	def add_cliente_logado(self):
		try:
			saveLoggedClients(self.__email)
		except Exception as error:
			print('\n', error)

class facade:

	#Função do facade que verifica se o cliente existe no banco
	#Também valida o email e a senha antes de verificar se o cliente existe
	@staticmethod
	def valida_cliente(email, senha):

		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		cliente_login = Verifica_Cliente(email, senha)

		fila = Fila_de_trabalho()

		comando1 = comando_verifica_login(cliente_login)
		comando2 = comando_verifica_senha(cliente_login)
		comando3 = comando_verifica_cliente(cliente_login)

		fila.adiciona(comando1)
		fila.adiciona(comando2)
		fila.adiciona(comando3)

		fila.processa()

		return cliente_login.status_cliente

	#Função que adiciona cliente no banco
	@staticmethod
	def add_cliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		cliente_cadastro = Adiciona_Cliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco)

		fila = Fila_de_trabalho()

		comando1 = comando_adiciona_cliente(cliente_cadastro)

		fila.adiciona(comando1)

		fila.processa()

	#Função que adiciona o cliente aos usuários logados
	@staticmethod
	def save_logged_clients(email):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		login_cliente = Clientes_Logados(email)

		fila = Fila_de_trabalho()

		comando1 = comando_cliente_logado(login_cliente)

		fila.adiciona(comando1)

		fila.processa()

	@staticmethod
	def relatorio_acesso():

		global horaPassada, tempoPassado

		horaAtual = datetime.now()
		#print('horaAtual:', horaAtual)
		#print('horaPassada:', horaPassada)

		tempoPassado = (horaAtual - horaPassada).seconds
		#print('tempoPassado:', tempoPassado)

		tempo = 600

		#Se o tempo que passou for maior que 10 minutos ele gera um relatorio
		if tempoPassado > tempo:
			#print('Iniciando a thread!')
			horaPassada = horaAtual
			threading.Timer(1, facade.gera_relatorio, args=[tempoPassado]).start()

	@staticmethod
	def gera_relatorio(tempoPassado):

		global frequenciaDeAcessoAnterior#, tempoPassado

		#print('Gerando Relatório!')
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		#print('Frequencia de Acesso Anterior:', frequenciaDeAcessoAnterior)

		frequenciaAtual = (frequenciaDeAcesso - frequenciaDeAcessoAnterior)

		frequenciaDeAcessoAnterior = frequenciaDeAcesso

		#print('Frequencia Atual:', frequenciaAtual)
		#print('Tempo Passado:', tempoPassado)

		if frequenciaAtual == 0:
			quantidadeAcessoSegundos = (tempoPassado/1)
		else:
			quantidadeAcessoSegundos = (tempoPassado/frequenciaAtual)

		#print('Quantidade Acesso Segundos:', quantidadeAcessoSegundos)

		minutosPassados = (tempoPassado/60)

		dados = [frequenciaAtual, minutosPassados, quantidadeAcessoSegundos]

		relatorio('json').getRelatorio(dados)

#Interface do Comando
class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass

#Fila de Execução dos comandos
class Fila_de_trabalho(object):
	def __init__(self):
		self.__comandos = []

	def adiciona(self, comando):
		self.__comandos.append(comando)

	def processa(self):
		for comando in self.__comandos:
			comando.executa()

#Comandos do Login
class comando_verifica_login(Comando):

	def __init__(self, verifica_cliente):
		self.__cliente_validado = verifica_cliente

	def executa(self):
		self.__cliente_validado.valida_login()

class comando_verifica_senha(Comando):

	def __init__(self, verifica_cliente):
		self.__cliente_validado = verifica_cliente

	def executa(self):
		self.__cliente_validado.valida_senha()

class comando_verifica_cliente(Comando):

	def __init__(self, verifica_cliente):
		self.__cliente_validado = verifica_cliente

	def executa(self):
		self.__cliente_validado.valida_cliente()

#Comandos para salvar usuário logado
class comando_cliente_logado(Comando):
	def __init__(self, clientes_logados):
		self.__login = clientes_logados

	def executa(self):
		self.__login.add_cliente_logado()

#Comandos do Cadastro
class comando_adiciona_cliente(Comando):
	def __init__(self, adiciona_cliente):
		self.__banco_cliente = adiciona_cliente

	def executa(self):
		self.__banco_cliente.adicionando()
