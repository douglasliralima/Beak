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

from business.control.addCliente import addCliente

import getpass
'''
while(True):
    try:
        nome = input("Digite seu nome completo")
        print("Senha deve ter no máximo 16 caracteres e  no mínimo 6  entre letras e numeros, com ao menos 1 número")
        senha = getpass.getpass("Digite sua senha:")
        print("Seu email de login deve ter no máximo 15 caracteres antes do @, " +
              "não pode ser vazio e não pode ter números")
        email = input("Digite seu email:")
        nascimento = input("Digite a sua data de nascimento:")
        cpf = input("Digite seu CPF:")
        rg = input("Digite seu RG")
        telefone = input("Digite seu Telefone:")
        endereco = input("Digite seu Endereço")
        
        addCliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco)
    except Exception as E:
    	print(E)'''