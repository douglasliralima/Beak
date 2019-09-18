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
from datetime import datetime

from business.model.cliente import Cliente
from infra import dao

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

    banco = 'shelve'
    gerenciador = dao.getBanco(banco)

    dict_log[email] = gerenciador.getCliente(email)

    with open('loggedClients.pck', 'wb') as arq:
        pickle.dump(dict_log, arq, pickle.HIGHEST_PROTOCOL)
        arq.close()

    printLoggedClients()

def printLoggedClients():
    dict_log = loadLoggedClients()

    list = []
    for user in dict_log:
        data = dict_log[user].getNascimento()
        list.append((data, dict_log[user].getNome()))

    list.sort(key=lambda date: datetime.strptime(date[0], "%d/%m/%Y"))

    print('\nLista Ordenada:', list)

def deleteLoggedClients(email):

    dict_log = loadLoggedClients()

    banco = 'shelve'
    gerenciador = dao.getBanco(banco)

    del dict_log[email]

    with open('loggedClients.pck', 'wb') as arq:
        pickle.dump(dict_log, arq, pickle.HIGHEST_PROTOCOL)
        arq.close()

    printLoggedClients()
