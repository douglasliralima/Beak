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

from business.FacadeGerenciamentoUsuario import FacadeGerenciamentoUsuario

import getpass

class login:
	def log_in(email, senha):

		try:
			cliente_valido = FacadeGerenciamentoUsuario.valida_cliente(email, senha)

			if cliente_valido:
				success_message = '\nLogin realizado com Sucesso!'
				print(success_message)
				FacadeGerenciamentoUsuario.save_logged_clients(email)
			else:
				fail_message = '\nFalha no Login, usuário inexistente!'
				print(fail_message)

		except Exception as error:
			print('\n', error)


def main():
	while(True):
		email = input('\n================\nDigite seu Login:\n================\n')
		senha = getpass.getpass('\n================\nDigite sua Senha:\n================\n')

		try:
			cliente_valido = FacadeGerenciamentoUsuario.valida_cliente(email, senha)

			if cliente_valido:
				success_message = '\nLogin realizado com Sucesso!'
				print(success_message)
				FacadeGerenciamentoUsuario.save_logged_clients(email)
			else:
				fail_message = '\nFalha no Login, usuário inexistente!'
				print(fail_message)

		except Exception as error:
			print('\n', error)

if __name__ == '__main__':
	main()
