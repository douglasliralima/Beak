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
from infra.infra import GerenciadorBanco


from business.model.cliente import Cliente
import getpass


def main():
    while(True):
        email = input('\n================\nDigite seu Login:\n================\n')
        senha = getpass.getpass('\n================\nDigite sua Senha:\n================\n')

        try:
            email = ValidaFormatoLogin().valida(email)
            senha = ValidaFormatoSenha().valida(senha)
            gerenciador = GerenciadorBanco()

            cliente_valido = gerenciador.validaCliente(email, senha)

            if cliente_valido:
                success_message = '\nLogin realizado com Sucesso!'
                print(success_message)
            else:
                fail_message = '\nFalha no Login, usuário inexistente!'
                print(fail_message)

        except Exception as error:
            print('\n', error)

if __name__ == '__main__':
    main()
