class Cliente:
	def __init__(self, nome, senha, email, nascimento, cpf, foto, telefone, cep, endereco):
		self.__nome = nome
		self.__senha = senha
		self.__email = email
		self.__nascimento = nascimento
		self.__cep = cep
		self.__cpf = cpf
		self.__foto = foto
		self.__telefone = telefone
		self.__endereco = endereco
		self.__servicos = []

	def getNome(self):
		return self.__nome

	def getSenha(self):
		return self.__senha

	def getEmail(self):
		return self.__email

	def getNascimento(self):
		return self.__nascimento

	def getCPF(self):
		return self.__cpf

	def getCEP(self):
		return self.__cep

	def getFoto(self):
		return self.__foto

	def getTelefone(self):
		return self.__telefone

	def getEndereco(self):
		return self.__endereco

	def getServicos(self):
		return self.__servicos

	def setSenha(self, novasenha):
		self.__senha = novasenha

	def setEmail(self, email):
		self.__email = email

	def setTelefone(self, telefone):
		self.__telefone = telefone

	def setEndereco(self, endereco):
		self.__endereco = endereco

	def setCEP(self, cep):
		self.__cep = cep

	def setNome(self, nome):
		self.__nome = nome

	def setFoto(self, foto):
		self.__foto = foto

	def addServico(self, servico):
		self.__servicos.append(servico)

	def excluiServico(self, servico):
		self.__servico.append()

	def __str__(self):
		return str(self.__nome + '\n' + self.__senha + '\n' + self.__email + '\n' + self.__nascimento + 
					'\n' + self.__cpf + '\n' + self.__cep + '\n' + self.__telefone + '\n' + self.__endereco)