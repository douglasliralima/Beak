import sys
from sys import platform as _platform

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

def add_cliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco):
    try:
        addCliente(nome, senha, email, dataNasc, cpf, rg, telefone, endereco)
    except Exception as E:
    	print(E)

def valida_login(email):
    try:
        email = ValidaFormatoLogin().valida(email.lower())
    except Exception as error:
        print('\n', error)

    return email

def valida_senha(senha):
    try:
        senha = ValidaFormatoSenha().valida(senha)
    except Exception as error:
        print('\n', error)

    return senha

def valida_cliente(email, senha):
    banco = 'shelve'
    gerenciador = dao.getBanco(banco)

    cliente_valido = False
    try:
        cliente_valido = gerenciador.validaCliente(email, senha)
    except Exception as error:
        print('\n', error)

    return cliente_valido

def save_logged_clients(email):
    try:
        saveLoggedClients(email)
    except Exception as error:
        print('\n', error)

def gera_relatorio():
    print('Gerando Relatório!')
