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

#classe que gera Relatório
from business import relatorio

frequenciaDeAcesso = 0
frequenciaDeAcessoAnterior = 0
tempoPassado = 0
horaPassada = datetime.now()

class facade:

	def add_cliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		try:
			addCliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco)
		except Exception as E:
			print(E)

	def valida_login(email):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		try:
			email = ValidaFormatoLogin().valida(email.lower())
		except Exception as error:
			print('\n', error)

		return email

	def valida_senha(senha):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		try:
			senha = ValidaFormatoSenha().valida(senha)
		except Exception as error:
			print('\n', error)

		return senha

	def valida_cliente(email, senha):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		banco = 'shelve'
		gerenciador = dao.getBanco(banco)

		cliente_valido = False
		try:
			cliente_valido = gerenciador.validaCliente(email, senha)
		except Exception as error:
			print('\n', error)

		return cliente_valido

	def save_logged_clients(email):
		global frequenciaDeAcesso
		frequenciaDeAcesso += 1
		#print('Frequencia de Acesso:', frequenciaDeAcesso)
		facade.relatorio_acesso()

		try:
			saveLoggedClients(email)
		except Exception as error:
			print('\n', error)

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

		relatorio.getRelatorio('json', dados)
