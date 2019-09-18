class ReceitaFederal:
    @staticmethod
    def validaCPF(cpf, dataNascimento):
        #11 digitos - CPF
        #9  digitos - Data
        if (dataNascimento == "00000000" and cpf == "00000000000"):
            return True
        else:
            return False