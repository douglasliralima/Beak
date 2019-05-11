import sys
import json
from sys import platform as _platform
from business.gerenciadoresRelatorio.templateRelatorio import templateRelatorio

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

class relatorio_json(templateRelatorio):

    def geraRelatorio(self, dados):
        #print('Dados:', dados)
        relatorio = {}
        relatorio['QuantidadeAcessos'] = dados[0]
        relatorio['MinutosPassados'] = dados[1]
        relatorio['Acesso/Segundos'] = dados[2]

        relatorio_json = json.dumps(relatorio, sort_keys=True)

        return relatorio_json
