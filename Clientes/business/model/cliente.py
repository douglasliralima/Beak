class Cliente:
	def __init__(self, nome, senha, email, nascimento, cpf, rg, telefone, endereco, user_id):
		self.__nome = nome
		self.__senha = senha
		self.__email = email
		self.__nascimento = nascimento
		self.__cpf = cpf
		self.__rg = rg
		self.__telefone = telefone
		self.__endereco = endereco
		self.__user_id = user_id
		self.__pedidos = []

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

	def getRG(self):
		return self.__rg

	def getTelefone(self):
		return self.__telefone

	def getEndereco(self):
		return self.__endereco

	def getUser_id(self):
		return self.__user_id

	def getPedidos(self):
		return self.__pedidos

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

	def setId(self, user_id):
		self.__id = user_id

	def addPedido(self, id_pedido):
		self.__pedidos.append(id_pedido)

	def __str__(self):
		return str(self.__nome + '\n' + self.__senha + '\n' + self.__email + '\n' + self.__nascimento +
					'\n' + self.__cpf + '\n' + self.__rg + '\n' + self.__telefone + '\n' + self.__endereco + '\n' + str(self.__user_id) + '\n' + self.__pedidos)
