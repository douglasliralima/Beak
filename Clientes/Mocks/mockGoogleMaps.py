class validadorReceitaFederal:
        
    def validaCPF(cpf, data):
        if (data == "00/00/0000" and cpf == "000.000.000"):
            return True
        else:
            return False