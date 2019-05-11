import sys
from sys import platform as _platform
from business.gerenciadoresRelatorio.templateRelatorio import templateRelatorio
from lxml import etree

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

class relatorio_html(templateRelatorio):

    def geraRelatorio(self, dados):
        # create XML 
        relatorio_xml = etree.Element('relatorioXML')
        quantidadeAcessos = etree.Element('quantidadeAcessos')
        quantidadeAcessos.text = str(dados[0])
        relatorio_xml.append(quantidadeAcessos)


        quantidadeAcessos = etree.Element('MinutosPassados')
        quantidadeAcessos.text = str(dados[1])
        relatorio_xml.append(quantidadeAcessos)


        quantidadeAcessos = etree.Element('AcessoSegundos')
        quantidadeAcessos.text = str(dados[2])
        relatorio_xml.append(quantidadeAcessos)

        return etree.tostring(relatorio_xml, pretty_print=True)

