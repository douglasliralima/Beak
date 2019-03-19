import shelve
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

from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha

from business.model.cliente import Cliente
import getpass

def credenciamento():

    filename = 'clientes.db'
    db = shelve.open(filename, flag='c')

    return db

def validaCliente(email, senha):

    #Pega o banco de dados de clientes já cadastrados
    db = credenciamento()

    try:
        cliente = db[email]
        cliente_valido = True
    except Exception as error:
        cliente_valido = False
        #print('Error:', error)

    return cliente_valido

def main():
    while(True):
        email = input('\n================\nDigite seu Login:\n================\n')
        senha = getpass.getpass('\n================\nDigite sua Senha:\n================\n')

        try:
            email = ValidaFormatoLogin().valida(email)
            senha = ValidaFormatoSenha().valida(senha)

            cliente_valido = validaCliente(email, senha)

            if cliente_valido:
                sucess_message = '\nLogin realizado com Sucesso!'
                print(sucess_message)
            else:
                fail_message = '\nFalha no Login, usuário inexistente!'
                print(fail_message)

        except Exception as error:
            print('\n', error)

if __name__ == '__main__':
    main()
