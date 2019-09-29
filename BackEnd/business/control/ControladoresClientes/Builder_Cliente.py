import os
import sys

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

from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha

from database.GerenciadorBancoShelve import GerenciadorBancoShelve

import uuid
from classes.cliente import Cliente

class Builder_Cliente(object):
	def __init__(self, nome, senha, email, dataNasc, cpf, foto, telefone, endereco):
		self._nome = nome
		self._senha = senha
		self._email = email
		self._dataNasc = dataNasc
		self._cpf = cpf
		self._foto = foto
		self._telefone = telefone
		self._endereco = endereco

	def adicionando(self):
		try:
		    banco = 'shelve'
		    self._email = ValidaFormatoLogin().valida(self._email)

		    self._senha = ValidaFormatoSenha().valida(self._senha)
		    gerenciador = GerenciadorBancoShelve()
		    print('Gerenciador:', gerenciador)

		    semiId = str(uuid.uuid4()).split('-')
		    user_id = str(self._cpf) + semiId[0] + semiId[1]

		    if gerenciador.validaEmail(self._email):
		        cliente = Cliente(self._nome, self._senha, self._email, self._dataNasc, self._cpf, self._foto, self._telefone, self._endereco, user_id)
		        gerenciador.persisteCliente(cliente)

		    gerenciador.closeDB()
		except Exception as E:
		    print(E)
