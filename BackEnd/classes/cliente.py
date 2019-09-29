class Cliente:
	def __init__(self, nome, senha, email, nascimento, cpf, foto, telefone, endereco):
		self.__nome = nome
		self.__senha = senha
		self.__email = email
		self.__nascimento = nascimento
		self.__cpf = cpf
		self.__foto = foto
		self.__telefone = telefone
		self.__endereco = endereco
		self.__id = None

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

	def getFoto(self):
		return self.__foto

	def getTelefone(self):
		return self.__telefone

	def getEndereco(self):
		return self.__endereco

	def getId(self):
		return self.__id

	def setSenha(self, novasenha):
		self.__senha = novasenha

	def setEmail(self, email):
		self.__email = email

	def setTelefone(self, telefone):
		self.__telefone = telefone

	def setEndereco(self, endereco):
		self.__endereco = endereco

	def setNome(self, nome):
		self.__nome = nome

	def setFoto(self, foto):
		self.__foto = foto

	def setId(self, uiid):
		self.__id = uiid

	def __str__(self):
		return str(self.__nome + '\n' + self.__senha + '\n' + self.__email + '\n' + self.__nascimento + 
					'\n' + self.__cpf + '\n' + self.__telefone + '\n' + self.__endereco)