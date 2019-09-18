class SistemaBancario:
    
    @staticmethod
    def usoBancario(banco, agencia, conta):
        #9 digitos zeros para RG
        #11 digitos zeros para CPF
        if (type(banco) == str and type(agencia) == str and type(conta) == str):
            return True
        else:
            return False