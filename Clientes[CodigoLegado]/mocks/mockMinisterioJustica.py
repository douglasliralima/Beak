class MinisterioJustica:
    
    @staticmethod   
    def AntecedenteCriminal(rg, cpf):
        #9 digitos zeros para RG
        #11 digitos zeros para CPF
        if (rg == "000000000" and cpf == "00000000000"):
            return True
        else:
            return False