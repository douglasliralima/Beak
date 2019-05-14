import numpy as np

from business.model.pedido import Pedido
from infra.communication.AdapterProfissionais import AdapterAvaliacaoProfissionais


class PedidoFinalizado(Pedido):
    def __init__(self, idPedido, descricao, imagens, dataPedido):
        super().__init__(idPedido, descricao, imagens)
        self._dataPedido = dataPedido
        self._avaliacao = 0

    def setAvaliacao(self, idProfissional, avaliacao):
        #Manda a avaliação para o profissional
        if AdapterAvaliacaoProfissionais.operacao(idProfissional, avaliacao):
            #Setta no pedido a avaliação do cliente
            self._avaliacao = avaliacao
            
    def __str__(self):
        return super().__str__() + str(self._avaliacao)