class AcimaLengthException(Exception):
    def __init__(self, tamCerto : int, tamErrado : int):
        #Declaramos os tipos privados abaixo:
        self.__tamCerto = tamCerto
        self.__tamErrado = tamErrado
        
    def __str__(self):
        return "Tamanho deveria ser acima de %i caracteres, foram passados %i"%(
                self.__tamCerto,self.__tamErrado)