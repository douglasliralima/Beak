class Email:
    @staticmethod
    def enviarEmail(email, texto):
        #9 digitos zeros para RG
        #11 digitos zeros para CPF
        if (email == "gmail"):
            return True
        else:
            return False

    @staticmethod   
    def recebimentoEmail():
        return "Email confirmado"