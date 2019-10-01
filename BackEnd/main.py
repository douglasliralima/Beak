import json
import pandas as pd
import numpy as np
import sys
import uuid
from datetime import datetime

from random import randrange, randint
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_cors import CORS
from waitress import serve



linux_origin_path = ".."
windows_origin_path = ".."

if (sys.platform == "linux" or sys.platform == "linux2") and linux_origin_path not in sys.path:
    sys.path.append(linux_origin_path)

if (sys.platform == "win32" or sys.platform == "win64") and windows_origin_path not in sys.path:
    sys.path.append(windows_origin_path)

from classes.cliente import Cliente
from classes.servico import Servico
from database.GerenciadorBancoShelve import GerenciadorBancoShelve
from database.servicoBD import servicoBD
from business.FacadeGerenciamentoUsuario import FacadeGerenciamentoUsuario
from checagem import Checagem

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'gledson'
sess = Session()
CORS(app)

def addSession(email):

    user_id = str(uuid.uuid4())
    cookies = request.cookies

    if 'session' in cookies:
        #user_id = cookies['session']
        old_id = cookies['session']
        if old_id in session:
            del session[old_id]
            session.modified = True
            #app.save_session(session)

    user = {}
    user['id'] = user_id
    json_user = json.dumps(user, sort_keys=True)

    #print('User ID:', user_id)
    #print('Session:', session.clear())
    if user_id in session:
        session.modified = True
        session[user_id] = {}
        #print('===Session:', session)

    else:
        session.modified = True
        session[user_id] = {}
        #print('Session with:', session)
    #print('Session:', session)

    session[user_id]['email'] = email
    print(session[user_id]['email'])

    return user_id

def getContext(userID):
    contextId = {}
    #contextId = session['users'][userID]
    #print("contextId:", contextId)
    if userID in session:
        contextId = session[userID]
        #print("contextId:", contextId)
    #print("contextId:", contextId)
    return contextId

def logoutUser(userID):
    ##print("userID no LOGOUT:", userID)
    #session.clear()
    #print('Session for Removed:', session)
    if userID in session:
        del session[userID]
        session.modified = True
        '''#app.save_session(session)
        #removed = session['users'].pop(userID)
        #print('Session for Removed:', session)
        #print('Removed from session:', removed)'''

def listaStatus(listaId, status):

    servico_bd = servicoBD()
    lista_status = []
    for servico_id in listaId:
        status_atual = servico_bd.retornaStatus(servico_id)

        if (status_atual == status):
            lista_status.append(servico_bd.getServico(servico_id))

    servico_bd.closeDB()

    return lista_status

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
    cep = str(dados['cep'])
    foto = str(dados['foto'])
    telefone = str(dados['telefone'])
    endereco = str(dados['endereco'])

    check = Checagem(nome, senha, senhaCheck, email, nascimento, cpf, cep, telefone)
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
            cliente = Cliente(nome, senha, email, nascimento, cpf, foto, telefone, cep, endereco)
            print(cliente)
            bd.persisteCliente(cliente)
            bd.closeDB()
            return "Cliente valido cadastrado"


    web_service_return_json = json.dumps(web_service_return)
    return web_service_return_json

@app.route("/login", methods=['POST'])
def login():
    print(request)
    print(request.data)
    print("\n\n\n\n\n\n\n")
    dados = request.get_json()
    email = str(dados['email'])
    senha = str(dados['senha'])

    print('email:', email)
    print('senha:', senha)

    #key = uuid.uuid4()
    web_service_return = {}

    bd = GerenciadorBancoShelve()
    cliente = None

    #cliente_valido = FacadeGerenciamentoUsuario.valida_cliente(email, senha)
    #print('cliente_valido:',cliente_valido)
    if bd.validaCliente(email, senha):
        cliente = bd.getCliente(email)
        key = addSession(email)
        web_service_return['nome'] = str(cliente.getNome())
        web_service_return['validation'] = True
        web_service_return['key'] = str(key)
    else:
        web_service_return['validation'] = False

    print("session: ", session)
    bd.closeDB()

    web_service_return_json = json.dumps(web_service_return)
    return web_service_return_json

@app.route("/novo-servico", methods=['POST'])
def novoServico():
    web_service_return = {}

    dados = request.get_json()
    uid = str(str(dados['uuid']))
    titulo = str(dados['titulo'])
    categoria = str(dados['categoria'])
    descricaoGeral = str(dados['descricaoGeral'])
    foto = str(dados['foto'])

    print("session:", session)

    if titulo != "":
        if descricaoGeral != "":
            context = getContext(uid)
            print("\n\n", context)
            email = context['email']

            print(email)

            id_servico = str(uuid.uuid4())

            bd_servico = servicoBD()
            bd_cliente = GerenciadorBancoShelve()

            cliente = bd_cliente.getCliente(email)
            servico = Servico(id_servico, cliente, titulo, categoria, descricaoGeral, foto)
            cliente.addServico(id_servico)
            bd_cliente.excluiCliente(email)
            bd_cliente.persisteCliente(cliente)
            bd_servico.persisteServico(servico)


            bd_servico.persisteServico(servico)
            bd_servico.closeDB()
            bd_cliente.closeDB()

            return "Busca cadastrada"
        else:
            web_service_return['descricaoGeral'] = "Campo vazio"
    else:
        web_service_return['titulo'] = "Campo vazio"

    web_service_return_json = json.dumps(web_service_return)
    return web_service_return_json

@app.route("/servico-cliente", methods=['GET'])
def clienteBuscas():
    print(request)
    print("Session servico cliente:", session)
    userID = request.args.get('key')
    context = getContext(uuid)
    email = context['email']

    bd_servico = servicoBD()
    bd_cliente = GerenciadorBancoShelve()

    id_servicos = bd_cliente.getCliente(email).getServicos()

    lista_servicos = listaStatus(id_servicos, "pendente")

    #Cria uma lista de json com todos os serviços
    data_servicos = {}
    data_servicos['servicos_listados'] = []
    for servico in lista_servicos:
        dados_servico = {}

        #Dados do Serviço
        dados_servico['date'] = servico.getData()
        dados_servico['categoria'] = servico.getCategoria()
        dados_servico['title'] = servico.getTitulo()
        dados_servico['description'] = servico.getDescricaoGeral()
        dados_servico['orçamentos'] = servico.getOrcamentos()
        dados_servico['visualizações'] = servico.getVisualizacoes()

        json_dados_servico = json.dumps(dados_servico, sort_keys=True)

        data_servicos['servicos_listados'].append(json_dados_servico)

    json_servicos = json.dumps(data_servicos, sort_keys=True)

    return json_servicos

@app.route("/nova-busca", methods=['POST'])
def novaBusca():
    print(request)
    print(request.data)
    return "Busca cadastrada"





if __name__ == '__main__':
    # Inicializa o servidor da aplicação:
    #app.run(host='localhost', port=5000)
    sess.init_app(app)
    serve(app, host = '0.0.0.0', port = 5000, threads=100)
