
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

import re

class ValidaFormatoLogin(Validacao):
    
    def valida(self, entrada):
        """
            Recebemos emails como logins, logo nós vamos ignorar tudo o que
            estiver após o @ e considerar que isso seria validado por uma 
            confirmação de cadastro
        """
        #Padrão perfeito
        padrao = re.match(r'^\b\D{1,15}(?=@)', entrada)

        if padrao:
            return entrada
        else:
            formatoInvalido = re.match(r'^\b.{0,15}(?=@)|[@].*', entrada)
            tamanhoInvalido = re.match(r'^\b.*(?=@)', entrada)
            if formatoInvalido:
                raise FormatoInvalidoException("Login deve ter no máximo " +
                                                "15 caracteres não pode ser" +
                                                " vazio e não pode ter números" )
            elif tamanhoInvalido:
                raise AbaixoLengthException(15, len(entrada))
            else:
                raise ErroFatal

#Testes
'''
try:
    validador = ValidaFormatoLogin()

    print(validador.valida("douglasfelizardoliralima@gmail.com.br"))

    print(validador.valida("douglasliralima@gmail.com"))

    print(validador.valida("douglaslira1997@gmail.com"))

    print(validador.valida("pouco@"))

    print(validador.valida("@hotmail.com"))

except Exception as E:
    print(E)

'''
