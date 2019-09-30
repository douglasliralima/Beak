import React from "react"
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";
import {BrowserRouter, Redirect} from "react-router-dom"

import NavBar from "../../components/navbarLogged/Navbar"
import "./NovaBusca.css"

import api from "../../service/api"

class NewPost extends React.Component {
    constructor(props){
        super(props);
        let campos = ["titulo", "categoria", "descricaoGeral"]
        let aux = {}
        for (let i in campos) {
            aux[campos[i]] = false
        }
        this.state = {
            cliente : this.props.location.state.key, //Cliente que está fazendo aquela busca
            errors : aux, //Booleans se cada campo está invalido
            errorsDescription : [], //Descrição do erro que aconteceu naquele campo
            formData : {}, //Dados a respeito do busca
            formSubmitted : false, //Boolean que diz se a busca foi ou não realizado
        };
    }
    

    handleInputChange = (event) => {
        //Pegando em quem ouve uma mudança
        const target = event.target;
        const value = target.value;
        const name = target.name;
        
        //Pegando o dicionário que temos e atribuindo o atual valor recebido
        let {formData} = this.state;

        formData[name] = value;
        // console.log(this.state.formData)
        console.log(formData)

        this.setState({formData : formData});
    }


     async BuscaForm(event){
        //Pega os dados do state e define a foto
        let {formData, cliente} = this.state;
        formData['foto'] = "fotinha.png"
        formData['cliente'] = cliente
        //Tenta cadastrar a busca e retorna a resposta do servidor
        return await api.post("nova-busca", formData, 
        { headers: { 'Content-Type': 'application/json' } })
        .then(function (res) {
            return res.data
        }).catch(function (err) {
            alert("Falha na conexão com servidor");
            window.location.reload()
            console.error(err);
            return false;
        });
    }

    busca = (e) => {
        e.preventDefault();

        //Primeiro vamos mandar ao servidor os dados no formulário para ele fazer o busca
        //Sucesso: Mensagem que o cliente foi cadastrado em caso de sucesso
        //Falha: Mensagens de quais foram os erros
        this.BuscaForm(e)
        .then((res) => {
            //Deixamos todas as flags falsas
            let {errors} = this.state;
            for (let error in errors){
                errors[error] = false
            }

            if (res == "Busca cadastrada") {
                alert("Sua busca foi cadastrada!");
                this.setState({
                    formSubmitted: true
                })
            } else {
                //Ligamos a flag de quais erros aconteceram
                for (let error in res) {
                    errors[error] = true;
                }
                this.setState({
                    errors : errors,
                    errorsDescription : res,
                })
            }
            window.location.reload()
        }).catch(function(err){
            console.error(err);
            // window.location.reload()
        });
    }

    render(){
        let {errors, errorsDescription, formSubmitted, cliente} = this.state;
        return (
        <div id = "Busca">
            <BrowserRouter>
                {/* <NavBar/> */}
                <h1>Criar uma nova busca</h1>
                <Form onSubmit={this.busca}>
                    <FormGroup>
                        <FormLabel><p className = "label">Nome</p></FormLabel>
                        <Form.Control  name="titulo" isInvalid = {errors['titulo']} onChange={this.handleInputChange} placeholder = "Digite o titulo"/>
                        <Form.Control.Feedback type="invalid">
                            {errorsDescription.titulo}
                        </Form.Control.Feedback>
                    </FormGroup>

                    <FormGroup>
                        <FormLabel><p className = "label">Categoria</p></FormLabel>
                        <Form.Control  name="categoria" onChange={this.handleInputChange} placeholder = "Digite a categoria" as = "select">
                            <option>Servicos Domesticos</option>
                            <option>Reparo Eletrodomesticos</option>
                            <option>Construcao Civil</option>
                            <option>Reparo e Carpintaria</option>
                            <option>Instalacao Eletrica</option>
                            <option>Assistencia Informatica</option>
                            <option>Servicos Encanamento</option>
                        </Form.Control>
                    </FormGroup>

                    <FormGroup>
                        <FormLabel><p className = "label">Descricao Geral</p></FormLabel>
                        <Form.Control  name="descricaoGeral" isInvalid = {errors['descricaoGeral']} onChange={this.handleInputChange} placeholder = "Digite a Descricao Geral"/>
                        <Form.Control.Feedback type="invalid">
                            {errorsDescription.descricaoGeral}
                        </Form.Control.Feedback>
                    </FormGroup>

                <Row>
                    <Col>
                        <Button type="submit" variant="warning">Buscar</Button>
                    </Col>
                </Row>
                </Form>
                {formSubmitted && <Redirect to= {{pathname : '/cliente', state : {key : cliente}}}/>}

            </BrowserRouter>
        </div>
        
        );
    }
}

export default NewPost;