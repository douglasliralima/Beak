
import sys

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	# linux
	origin_path = "/../.."
elif _platform == "win32" or "win64":
	# Windows
	origin_path = "..\.."
#elif _platform == "darwin":
	# MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha
import shelve

from business.model.cliente import Cliente

import re

filename = 'clientes.db'


def addCliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco):
	email = ValidaFormatoLogin().valida(email)
	senha = ValidaFormatoSenha().valida(senha)

	cliente = Cliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco)


## MANDAR O QUE TEM ABAIXO PRA INFRA DEPOIS
## TESTE
	db = shelve.open(filename, flag='c')
	db[email] = cliente
	db.close()