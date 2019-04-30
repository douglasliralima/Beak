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

print('origin_path:', sys.path)
if origin_path not in sys.path:
    sys.path.append(origin_path)

from business import facade

import getpass

facade.add_cliente('Douglas Felizardo', '1a3b4c6', "douglasliralima@gmail.com", '26/10/1997',
							'465465462', '12545452', '839982154', 'rua adalto lemos, 18')

facade.add_cliente('Ewerton Santos', 'abcde1', "ewertondnsantos@gmail.com", '11/01/1997',
							'78945612345', '3998875', '83986288483', 'rua doutor júlio queiroz carreira, 51')

facade.add_cliente('Pedro de Abrantes', 'abcde1', "pedroabrantes@gmail.com", '09/04/1994',
							'78945612345', '3998875', '83999821584', 'rua maria rosa, 1410')

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
    	print(E)
'''
