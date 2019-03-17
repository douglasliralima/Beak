#Colocar o caminho do control raiz relativo ao arquivo:
import sys
origin_path = "/.."
if origin_path not in sys.path:
    sys.path.append(origin_path)

from Validacoes.Validacao import Validacao
from Exceptions.FormatoInvalidoException import FormatoInvalidoException
from Exceptions.AbaixoLengthException import AbaixoLengthException
from Exceptions.ErroFatal import ErroFatal

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
            return True
        else:
            formatoInvalido = re.match(r'^\b.{0,15}(?=@)|[@].*', entrada)
            tamanhoInvalido = re.match(r'^\b.*(?=@)', entrada)
            if formatoInvalido:
                raise FormatoInvalidoException("Login deve ter no máximo " +
                                                "15 caracteres não pode ser" +
                                                "vazio e não pode ter números" )
            elif tamanhoInvalido:
                raise AbaixoLengthException(15, len(entrada))
            else:
                raise ErroFatal
'''
Testes
validador = ValidaFormatoLogin()

print(validador.valida("douglasfelizardoliralima@gmail.com.br"))

print(validador.valida("douglasliralima@gmail.com"))

print(validador.valida("douglaslira1997@gmail.com"))

print(validador.valida("pouco@"))

print(validador.valida("@hotmail.com"))
'''

