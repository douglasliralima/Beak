#Colocar o caminho do control raiz relativo ao arquivo:
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

from business.control.Validacoes.Validacao import Validacao
from business.control.Exceptions.FormatoInvalidoException import FormatoInvalidoException
from business.control.Exceptions.AbaixoLengthException import AbaixoLengthException
from business.control.Exceptions.ErroFatal import ErroFatal
from business.control.Exceptions.AcimaLengthException import AcimaLengthException

import re

class ValidaFormatoSenha(Validacao):
    
    def valida(self, entrada):
        """
            Recebemos emails como logins, logo nós vamos ignorar tudo o que
            estiver após o @ e considerar que isso seria validado por uma 
            confirmação de cadastro
        """
        #Padrão perfeito
        padrao = re.match(r'^(?=\w*\d)[a-zA-Z\d]{5,15}$', entrada)

        if padrao:
            return entrada
        else:
            formatoInvalido = re.match(r'^.{6,16}$', entrada)
            tamanhoMenor = re.match(r'^[a-zA-Z\d]{0,5}$', entrada)
            tamanhoMaior = re.match(r'^[a-zA-Z\d]+$', entrada)
            if formatoInvalido:
                raise FormatoInvalidoException("Senha deve ter no máximo " +
                                               "16 caracteres e  no mínimo" +
                                               " 6 caracteres entre letras" +
                                               "e ao menos 1 número." )
            elif tamanhoMenor:
                raise AcimaLengthException(5, len(entrada))
            elif tamanhoMaior:
                raise AbaixoLengthException(15, len(entrada))
            else:
                raise ErroFatal
                
'''
testes
validador = ValidaFormatoSenha()

print("Tamanho mínimo - Só número", validador.valida("123456"))

print("Tamanho máximo - Só número", validador.valida("123456789012356"))

print("Tamanho mínimo - mix", validador.valida("1a3b4c6"))

print("Vazio", validador.valida(""))

print("Apenas Letras", validador.valida("asdasdasdasd"))

print("1 letra, 1 numero", validador.valida("a1"))

print("5 letras 1 numero", validador.valida("asdasd1"))

print("Tamanho máximo além - Só numero", validador.valida("1234dasdasd567890123456789"))

'''