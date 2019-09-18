class Profissionais:
    
    @staticmethod   
    def confirmaServico(idProfissional):
        #9 digitos zeros para RG
        #11 digitos zeros para CPF
        if (idProfissional != None):
            return True
        else:
            return False

    @staticmethod   
    def pagamento(idProfissional, idServico):
        #9 digitos zeros para RG
        #11 digitos zeros para CPF
        if (idProfissional != None and idServico != None):
            return True
        else:
            return False

    @staticmethod
    def avaliacaoServico(idProfissional, avaliacao):
        if (idProfissional != None and avaliacao != None):
            return True
        else:
            return False
