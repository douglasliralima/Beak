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

import pickle
import collections

from business.model.cliente import Cliente
from infra.infra import GerenciadorBanco 

def loadLoggedClients():
    try:
        with open('loggedClients.pck', 'rb') as arq:
            dict_log = pickle.load(arq)
            arq.close()
    except Exception:
        return collections.OrderedDict()

    return dict_log

def saveLoggedClients(email):

    dict_log = loadLoggedClients()

    gerenciador = GerenciadorBanco()

    dict_log[email] = gerenciador.getCliente(email)

    with open('loggedClients.pck', 'wb') as arq:
        pickle.dump(dict_log, arq, pickle.HIGHEST_PROTOCOL)
        arq.close()

    printLoggedClients()

def printLoggedClients():
    dict_log = loadLoggedClients()

    print('Dict_log:', dict_log)

def deleteLoggedClients(email):

    arq = open("loggedClients.pck", 'rb')

    pickle.dump(email, arq)
    arq.close()
