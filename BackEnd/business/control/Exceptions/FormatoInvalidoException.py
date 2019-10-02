class FormatoInvalidoException(Exception):
    
    def __init__(self, descricaoFormatoCorreto : str):
        self.__descricaoFormatoCorreto = descricaoFormatoCorreto
        
    def __str__(self):
        return "Formato invalido: %s"%(self.__descricaoFormatoCorreto)