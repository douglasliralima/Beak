from business.control.pedidos.pedidoAberto import PedidoAberto
import uuid
from infra import dao

import numpy as np
cpf = 000000
semiId = str(uuid.uuid4()).split('-')
user_id = str(cpf) + semiId[0] + semiId[1]

imagens = np.array([[[1,2],[3,4]],[[1,2],[3,4]],[[1,2],[3,4]]])

pedido = PedidoAberto(user_id, "Eu quero que lavem a minha louça!", imagens)

print(pedido.__str__())

pedido = pedido.aceitarOrcamento(1, "01/15/2018")

print(pedido.__str__(), type(pedido))

pedido = pedido.finalizarPagamento(1, "dinheiro")

pedido.setAvaliacao(1, 10)

print(pedido.__str__())
