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

from business.control.addCliente import addCliente

import re


try:
	addCliente('Douglas Felizardo', '1a3b4c6', "douglasliralima@gmail.com", '26/10/1997',
								'465465462', '12545452', '839982154', 'rua adalto lemos, 18')

	addCliente('Ewerton Santos', 'abcde1', "ewertondnsantos@gmail.com", '11/01/1997',
								'78945612345', '3998875', '83986288483', 'rua doutor júlio queiroz carreira, 51')
except Exception as E:
	print(E)

filename = 'clientes.db'
db = shelve.open(filename, flag='c')
cliente1 = db['douglasliralima@gmail.com']
cliente2 = db['ewertondnsantos@gmail.com']
print(cliente1)
print('\n')
print(cliente2)
