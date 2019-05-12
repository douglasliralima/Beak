
import sys

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
	# linux
	origin_path = "/../.."
elif _platform == "win32" or "win64":
	# Windows
	origin_path = "..\.."
#elif _platform == "darwin":
	# MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

from business.control.Validacoes.ValidaLogin import ValidaFormatoLogin
from business.control.Validacoes.ValidaSenha import ValidaFormatoSenha

from infra import dao
import uuid
from business.model.cliente import Cliente

def addCliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco):
    banco = 'shelve'

    email = ValidaFormatoLogin().valida(email)

    senha = ValidaFormatoSenha().valida(senha)
    gerenciador = dao.getBanco(banco)
    print('Gerenciador:', gerenciador)

    semiId = str(uuid.uuid4()).split('-')
    user_id = str(cpf) + semiId[0] + semiId[1]

    if gerenciador.validaEmail(email):
        cliente = Cliente(nome, senha, email, nascimento, cpf, rg, telefone, endereco, user_id)
        gerenciador.persisteCliente(cliente)

    gerenciador.closeDB()
