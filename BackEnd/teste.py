import re

def checkCPF(cpf):
	check = False
	causa = ""

	if cpf != "":
		if re.match(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$', cpf):
			return True, causa
		else:
			causa = "Formato inválido de CPF"
			return False, causa
	else:
		causa = "CPF vazio"
		return False, causa

def checkNome(nome):
	check = False
	causa = ""
	if nome != "":
		if re.match(r'[A-Za-z]{2,25}||\s[A-Za-z]{2,25}$', nome):
			return True, causa
		else:
			causa = "Formato inválido de Nome"
			return False, causa
	else:
		causa = "Nome vazio"
		return False, causa


def checkSenha(senha, senhaCheck):
	check = False
	causa = ""

	if senha != "" and senhaCheck != "":
		if senha == senhaCheck:
			return True, causa
		else:
			causa = "Senhas não batem"
			return False, causa

	else:
		causa = "Senha vazia"
		return False, causa

def checkEmail(email):
	check = False
	causa = ""

	if email != "":
		if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
			return True, causa
		else:
			causa = "Formato inválido de email"
			return False, causa
	else:
		causa = "Email vazio"
		return False, causa

def checkNascimento(nascimento):
	check = False
	causa = ""

	if nascimento != "":
		if re.match(r'[0-9]{2}/[0-9]{2}/[0-9]{4}$', nascimento):
			return True, causa
		else:
			causa = "Formato inválido de data de nascimento"
			return False, causa
	else:
		causa = "Data de nascimento vazio"
		return False, causa

def checkTelefone(telefone):
	check = False
	causa = ""

	if telefone != "":
		if re.match(r'[0-9]{11}$', telefone):
			return True, causa
		else:
			causa = "Formato inválido de telefone"
			return False, causa
	else:
		causa = "Telefone vazio"
		return False, causa

nome = "Pedro Abrantes"
senha = "123"
senhaCheck = "12345"
email = "pedro.abrantes94@gmail.com"
nascimento = "09/04/2001"
cpf = "065.124.381-71"
telefone = "08399821584"

print(checkCPF(cpf))
print(checkNome(nome))
print(checkSenha(senha, senhaCheck))
print(checkEmail(email))
print(checkNascimento(nascimento))
print(checkTelefone(telefone))

web_service_return = {}

if web_service_return:
	result = False

print("\n", web_service_return, type(web_service_return), result)

