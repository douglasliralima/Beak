import numpy as np

from business.model.pedido import Pedido
from business.control.pedidos.pedidoFinalizado import PedidoFinalizado
from infra.communication.AdapterProfissionais import AdapterPagamentoProfissionais


class PedidoAndamento(Pedido):
    def __init__(self, idPedido, descricao, imagens, dataPedido,
                 fonte, zelador):
        super().__init__(idPedido, descricao, imagens)
        self._dataPedido = dataPedido
        self.__fonte = fonte
        self.__zelador = zelador

    def getDataPedido(self):
        return self._dataPedido
    
    def cancelamentoPedido(self):
        from business.control.pedidos.pedidoAberto import PedidoAberto
        self.__fonte = self.__zelador.getFonte()
        state = self.__fonte.get_state()

        self._descricao = state.getDescricao()
        self._imagens = state.getImagens()
        self._idPedido = state.getId()
    
        return PedidoAberto(self._idPedido, self._descricao, self._imagens)

    def finalizarPagamento(self, idProfissional, modalidade):
        if modalidade == "dinheiro":
            return PedidoFinalizado(self._idPedido, self._descricao, 
                                    self._imagens, self._dataPedido)
        else:
            #Realiza o pagamento
            if AdapterPagamentoProfissionais.operacao(idProfissional, self._idPedido):
                #Retorna o próximo estado do pedido
                return PedidoFinalizado(self._idPedido, self._descricao,
                                        self._imagens, self._dataPedido)