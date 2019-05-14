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

#Funções chamadas em Login
from business.model.cliente import Cliente

#Importando biblioteca para o Command
from abc import ABC, abstractmethod, ABCMeta

#classe que gera Relatório
from business.relatorio import relatorio

#Imports dos comandos que serão utilizados
from business.control.Commands.Comando import Comando
from business.control.Commands.CadeiaComandos import Fila_de_trabalho
from business.control.Commands.ComandoVerificaLogin import comando_verifica_login
from business.control.Commands.ComandoVerificaSenha import comando_verifica_senha
from business.control.Commands.ComandoValidaCliente import comando_verifica_cliente
from business.control.Commands.ComandoAdicionaCliente import comando_adiciona_cliente
from business.control.Commands.ComandoClienteLogado import comando_cliente_logado

#Banco que estamos usando
frequenciaDeAcesso = 0
frequenciaDeAcessoAnterior = 0
tempoPassado = 0
horaPassada = datetime.now()

#Classes de controle
from business.control.ControladoresClientes.Verifica_Cliente import Verifica_Cliente
from business.control.ControladoresClientes.Builder_Cliente import Builder_Cliente
from business.control.ControladoresClientes.Cliente_Logados import Clientes_Logados

class FacadeCadastro:

	#Função do FacadeCadastro que verifica se o cliente existe no banco
	#Também valida o email e a senha antes de verificar se o cliente existe
	@staticmethod
	def valida_cliente(email, senha):

		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		FacadeCadastro.relatorio_acesso()

		cliente_login = Verifica_Cliente(email, senha)

		fila = Fila_de_trabalho()

		comando1 = comando_verifica_login(cliente_login)
		comando2 = comando_verifica_senha(cliente_login)
		comando3 = comando_verifica_cliente(cliente_login)

		fila.adiciona(comando1)
		fila.adiciona(comando2)
		fila.adiciona(comando3)

		fila.processa()
		result = Verifica_Cliente.status_cliente

		return result

	#Função que adiciona cliente no banco
	@staticmethod
	def add_cliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		FacadeCadastro.relatorio_acesso()

		cliente_cadastro = Builder_Cliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco)

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
		FacadeCadastro.relatorio_acesso()

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
			threading.Timer(1, FacadeCadastro.gera_relatorio, args=[tempoPassado]).start()

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
