import numpy as np

class Pedido:
	def __init__(self, idPedido, descricao, imagens):
		self._idPedido = idPedido
		self._descricao = descricao
		self._imagens = imagens
		self._dataPedido = "00/00/0000"
		
	def getId(self):
    		return self._idPedido

	def getDescricao(self):
    		return self._descricao

	def getImagens(self):
    		return self._imagens

	def setId(self, id):
		self._idPedido = id


	def __str__(self):
		return str(self._idPedido + '\n' + self._descricao + '\n'  + self._dataPedido + '\n')


'''
	pedido_aberto:
		Mudar a descrição
		Adicionar imagem
		Remover imagem
		Aceitar orçamento(Define a data que vai acontecer)


	pedido_andamento:
		Data que vai acontecer
		Cancelar

	pedido_finalizado:
		Definir a nota do profissional
'''
