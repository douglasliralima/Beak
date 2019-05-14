import numpy as np

from business.model.pedido import Pedido
from infra.communication.AdapterProfissionais import AdapterConfirmaProfissionais


from business.control.Fonte import Fonte
from business.control.Memento import Memento
from business.control.Zelador import Zelador

class PedidoAberto(Pedido):
    def __init__(self, idPedido, descricao, imagens):
        super().__init__(idPedido, descricao, imagens)
        self.__fonte = None
        self.__flagFonte = True
        self.__zelador = None
        
    def criaFonte(self):
        if self.__flagFonte:
                self.__fonte = Fonte(PedidoAberto(self._idPedido, self._descricao, self._imagens))
                self.__zelador = Zelador(self.__fonte)
                self.__flagFonte = False
            
    def mudarDescrição(self, novaDescricao):
        self.criaFonte()
        self.__zelador.save_state(PedidoAberto(self._idPedido, self._descricao, self._imagens))
        self._descricao = novaDescricao
    
    def adicionaImagem(self, imagem):
        self.criaFonte()
        self.__zelador.save_state(PedidoAberto(self._idPedido, self._descricao, self._imagens))
        self._imagens = np.append(self._imagens, imagem, axis=0)

    def removeImagem(self, indice):
        self.criaFonte()
        self.__zelador.save_state(PedidoAberto(self._idPedido, self._descricao, self._imagens))
        indice = [indice]
        self._dataPedido = np.delete(self._dataPedido, indice, axis = 0)


    def previous_state(self):
        self.criaFonte()
        self.__zelador.undo_state()
        self.__fonte = self.__zelador.getFonte()
        state = self.__fonte.get_state()

        self._descricao = state.getDescricao()
        self._imagens = state.getImagens()
        self._idPedido = state.getId()

    '''
    Vamos mandar para a API profissionais um sinal de que o serviço daquele mano foi
    aceito e, a partir do orçamento, definimos o dia que será realizado o trabaio
    '''
    #Aceitar orçamento de profissional, 
    def aceitarOrcamento(self, idProfissional, dataOrcamento):
        self.criaFonte()
        self.__zelador.save_state(PedidoAberto(self._idPedido, self._descricao, self._imagens))
        from business.control.pedidos.pedidoAndamento import PedidoAndamento

        if AdapterConfirmaProfissionais.operacao(idProfissional):

            return PedidoAndamento(self._idPedido, self._descricao, 
                                    self._imagens, dataOrcamento,
                                    self.__fonte, self.__zelador)
        else:
            print("Resposta retornou false da API profissionais")
            raise Exception
            #self.__dataPedido = 
