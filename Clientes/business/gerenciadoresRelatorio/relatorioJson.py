import sys
from sys import platform as _platform
import json

if _platform == "linux" or _platform == "linux2":
	# linux
	origin_path = "/.."
elif _platform == "win32" or "win64":
	# Windows
	origin_path = ".."
#elif _platform == "darwin":
	# MAC OS X

#print('origin_path:', sys.path)
if origin_path not in sys.path:
	sys.path.append(origin_path)

def geraRelatorio(dados):
    #print('Dados:', dados)
    relatorio = {}
    relatorio['QuantidadeAcessos'] = dados[0]
    relatorio['MinutosPassados'] = dados[1]
    relatorio['Acesso/Segundos'] = dados[2]

    relatorio_json = json.dumps(relatorio, sort_keys=True)

    return relatorio_json
