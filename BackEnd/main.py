import json
import pandas as pd
import numpy as np
import sys
import uuid

from random import randrange, randint
from flask import Flask, render_template, request

linux_origin_path = ".."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from classes.cliente import Cliente
from database.GerenciadorBancoShelve import GerenciadorBancoShelve
from business.FacadeGerenciamentoUsuario import FacadeGerenciamentoUsuario
from checagem import Checagem

app = Flask(__name__)


@app.route("/cadastro-cliente", methods=['POST'])
def cadastroCliente():
    web_service_return = {}
    #try:
        # Transforma os dados do formato json para um dicionário python:
    dados = request.get_json()
    nome = str(dados['nome'])
    senha = str(dados['senha'])
    senhaCheck = str(dados['senhaCheck'])
    email = str(dados['email'])
    nascimento = str(dados['nascimento'])
    cpf = str(dados['cpf'])
    foto = str(dados['foto'])
    telefone = str(dados['telefone'])
    endereco = str(dados['endereco'])

    check = Checagem(nome, senha, senhaCheck, email, nascimento, cpf, telefone)
    bd = GerenciadorBancoShelve()

    checagem, causa, campo = check.run()

    print(checagem, causa, campo)

    print("'", check.nome, "'")



    if bd.validaEmail(email):
        for i in range(len(checagem)):
            if checagem[i]:
                continue
            else:
                web_service_return[campo[i]] = causa[i]
        if not web_service_return:
            cliente = Cliente(nome, senha, email, nascimento, cpf, foto, telefone, endereco)
            print(cliente)
            bd.persisteCliente(cliente)
            bd.closeDB()
            return "Cliente valido cadastrado"


    web_service_return_json = json.dumps(web_service_return)
    return web_service_return_json

@app.route("/login", methods=['GET'])
def login():
    dados = request.get_json()
    email = str(dados['email'])
    senha = str(dados['senha'])

    print('email:', email)
    print('senha:', senha)

    key = uuid.uuid4()
    web_service_return = {}

    bd = GerenciadorBancoShelve()
    cliente = None

    cliente_valido = FacadeGerenciamentoUsuario.valida_cliente(email, senha)
    print('cliente_valido:',cliente_valido)
    if cliente_valido:
        cliente = bd.getCliente(email)

        web_service_return['nome'] = str(cliente.getNome())
        web_service_return['validation'] = True
        web_service_return['key'] = str(key)


    bd.closeDB()

    web_service_return_json = json.dumps(web_service_return)
    return web_service_return_json
    #return cliente

if __name__ == '__main__':
    # Inicializa o servidor da aplicação:
    #app.run(host='0.0.0.0', port=3000)
    app.run()