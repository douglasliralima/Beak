from classes.cliente import Cliente
from database.GerenciadorBancoShelve import GerenciadorBancoShelve
from business.FacadeGerenciamentoUsuario import FacadeGerenciamentoUsuario

import re

class Checagem:
	def __init__(self, nome, senha, senhaCheck, email, nascimento, cpf, cep, telefone):
		self.nome = nome
		self.senha = senha
		self.senhaCheck = senhaCheck
		self.email = email
		self.nascimento = nascimento
		self.cpf = cpf
		self.cep = cep
		self.telefone = telefone



	def checkCPF(self):
		check = False
		causa = ""

		if self.cpf != "":
			if re.match(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$', self.cpf):
				return True, causa, "cpf"
			else:
				causa = "Formato invalido de CPF"
				return False, causa, "cpf"
		else:
			causa = "CPF vazio"
			return False, causa, "cpf"

	def checkCEP(self):
		check = False
		causa = ""

		if self.cep != "":
			if re.match(r'[0-9]{5}-[\d]{3}$', self.cep):
				return True, causa, "cep"
			else:
				causa = "Formato invalido de CEP"
				return False, causa, "cep"
		else:
			causa = "CEP vazio"
			return False, causa, "cep"

	def checkNome(self):
		check = False
		causa = ""
		if self.nome != "":
			if re.match(r'[A-Za-z]{2,25}||\s[A-Za-z]{2,25}$', self.nome):
				return True, causa, "nome"
			else:
				causa = "Formato invalido de Nome"
				return False, causa, "nome"
		else:
			causa = "Nome vazio"
			return False, causa, "nome"


	def checkSenha(self):
		check = False
		causa = ""

		if self.senha != "" and self.senhaCheck != "":
			if self.senha == self.senhaCheck:
				if len(self.senha) < 5 or len(self.senha) > 16:
					causa = "Senha deve estar entre 5 e 16 digitos"
					return False, causa, "senha"
				else:
					return True, causa, "senha"
			else:
				causa = "Senhas nao batem"
				return False, causa, "senha"

		else:
			causa = "Senha vazia"
			return False, causa, "senha"

	def checkEmail(self):
		check = False
		causa = ""

		if self.email != "":
			if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email):
				return True, causa, "email"
			else:
				causa = "Formato invalido de email"
				return False, causa, "email"
		else:
			causa = "Email vazio"
			return False, causa, "email"

	def checkNascimento(self):
		check = False
		causa = ""

		if self.nascimento != "":
			if re.match(r'[0-9]{2}/[0-9]{2}/[0-9]{4}$', self.nascimento):
				return True, causa, "nascimento"
			else:
				causa = "Formato invalido de data de nascimento"
				return False, causa, "nascimento"
		else:
			causa = "Data de nascimento vazio"
			return False, causa, "nascimento"

	def checkTelefone(self):
		check = False
		causa = ""

		if self.telefone != "":
			if re.match(r'[0-9]{12}$', self.telefone):
				return True, causa, "telefone"
			else:
				causa = "Formato invalido de telefone"
				return False, causa, "telefone"
		else:
			causa = "Telefone vazio"
			return False, causa, "telefone"


	def run(self):
		checagem = []
		causa = []
		nome = []

		ch, motivo, n = self.checkCPF()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		ch, motivo, n = self.checkCEP()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		ch, motivo, n = self.checkNome()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		ch, motivo, n = self.checkSenha()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		ch, motivo, n = self.checkEmail()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		ch, motivo, n = self.checkNascimento()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		ch, motivo, n = self.checkTelefone()
		checagem.append(ch)
		causa.append(motivo)
		nome.append(n)

		return checagem, causa, nome