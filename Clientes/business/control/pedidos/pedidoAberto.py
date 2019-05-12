import numpy as np

from business.model.pedido import Pedido
from infra.communication.AdapterProfissionais import AdapterConfirmaProfissionais


class PedidoAberto(Pedido):
    def __init__(self, idPedido, descricao, imagens):
        super().__init__(idPedido, descricao, imagens)

    def mudarDescrição(self, novaDescricao):
        self._descricao = novaDescricao
    
    def adicionaImagem(self, imagem):
        self._imagens = np.append(self._imagens, imagem, axis=0)

    def removeImagem(self, indice):
        indice = [indice]
        self._dataPedido = np.delete(self._dataPedido, indice, axis = 0)

    '''
    Vamos mandar para a API profissionais um sinal de que o serviço daquele mano foi
    aceito e, a partir do orçamento, definimos o dia que será realizado o trabaio
    '''
    #Aceitar orçamento de profissional, 
    def aceitarOrcamento(self, idProfissional, dataOrcamento):
        from business.control.pedidos.pedidoAndamento import PedidoAndamento

        if AdapterConfirmaProfissionais.operacao(idProfissional):

            return PedidoAndamento(self._idPedido, self._descricao, 
                                    self._imagens, dataOrcamento)
        else:
            print("Resposta retornou false da API profissionais")
            raise Exception
            #self.__dataPedido = 
