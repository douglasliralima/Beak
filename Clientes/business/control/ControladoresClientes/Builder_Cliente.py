from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha

from infra import dao
import uuid
from business.model.cliente import Cliente

class Builder_Cliente(object):
	def __init__(self, nome, senha, email, dataNasc, cpf, rg, telefone, endereco):
		self._nome = nome
		self._senha = senha
		self._email = email
		self._dataNasc = dataNasc
		self._cpf = cpf
		self._rg = rg
		self._telefone = telefone
		self._endereco = endereco

	def adicionando(self):
		try:
		    banco = 'shelve'
		    self._email = ValidaFormatoLogin().valida(self._email)

		    self._senha = ValidaFormatoSenha().valida(self._senha)
		    gerenciador = dao.getBanco(banco)
		    print('Gerenciador:', gerenciador)

		    semiId = str(uuid.uuid4()).split('-')
		    user_id = str(self._cpf) + semiId[0] + semiId[1]

		    if gerenciador.validaEmail(self._email):
		        cliente = Cliente(self._nome, self._senha, self._email, self._dataNasc, self._cpf, self._rg, self._telefone, self._endereco, user_id)
		        gerenciador.persisteCliente(cliente)

		    gerenciador.closeDB()
		except Exception as E:
		    print(E)