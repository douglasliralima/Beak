import os
import sys

from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    # linux
    origin_path = "../../.."
elif _platform == "win32" or "win64":
    # Windows
    origin_path = "..\..\.."
#elif _platform == "darwin":
    # MAC OS X

if origin_path not in sys.path:
    sys.path.append(origin_path)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "\..")

#from business.control.Exceptions.ClienteInexistenteException import ClienteInexistenteException
#from business.control.Exceptions.EmailExistenteException import EmailExistenteException
import shelve

from GerenciadorBancoShelve import GerenciadorBancoShelve
from classes.cliente import Cliente

filename = os.path.dirname(os.path.abspath(__file__)) + "/clientes.db"
         #filename = 'clientes.db'
db = shelve.open(filename, flag='c')
#db = shelve.open("clientes.db")
email = "pedro.abrantes94@gmail.com"

print(list(db.keys()))

if email in list(db.keys()):
	print("True")

#print(cliente.getNome())
db.close()