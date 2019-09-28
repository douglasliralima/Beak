import React from "react";
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";

// import {isEmpty} from '../../shared/validator';
import api from "../../service/api"

import NavBar from "../../components/navbarUnlogged/navbar.js"
import "./Cadastro.css";

class Cadastro extends React.Component {
    constructor(props){
        super(props);
        let campos = ["email", "senha", "senhaCheck", "cep", "endereco"]
        let aux = {}
        for (let i in campos) {
            aux[campos[i]] = false
        }
        this.state = {
            formData : {}, //Dados a respeito do cadastro
            errors : aux, //Booleans se cada campo está invalido
            errorsDescription : [], //Descrição do erro que aconteceu naquele campo
            formSubmitted : false, //Boolean que diz se o cadastro foi ou não realizado
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

        this.setState({formData : formData});
    }


     async CadastraForm(event){
        //Pega os dados do state e define a foto
        let {formData} = this.state;
        formData['foto'] = "eu.png"

        //Tenta cadastrar o cliente e retorna a resposta do servidor
        return await api.post("cadastro-cliente", formData)
        .then(function (res) {
            return res.data
        }).catch(function (err) {
            alert("Falha na conexão com servidor");
            window.location.reload()
            console.error(err);
            return false;
        });
    }

    cadastro = (e) => {
        e.preventDefault();

        //Primeiro vamos mandar ao servidor os dados no formulário para ele fazer o cadastro
        //Sucesso: Mensagem que o cliente foi cadastrado em caso de sucesso
        //Falha: Mensagens de quais foram os erros
        let errorsDescription = this.CadastraForm(e)
        .then(function (res){
            return res
        }).catch(function(err){
            console.error(err);
            // window.location.reload()
        });

        //Deixamos todas as flags falsas
        let {errors} = this.state;
        for (let error in errors){
            errors[error] = false
        }
        
        console.log("ErrorDescription: " + errorsDescription)
        if (errorsDescription == "Cliente valido cadastrado") {
            alert("Você foi cadastrado!");
            window.location.reload()
        } 
        else {
            //Ligamos a flag de quais erros aconteceram
            for (let error in errorsDescription) {
                errors[error] = true;
            }
            this.setState({
                errors : errors,
                errorsDescription : errorsDescription,
                formSubmitted: true
            })
        }
        console.log(errors);
    }

    render(){
        const {errors, errorsDescription} = this.state;
        return (
        <div id = "Cadastro">
            <NavBar/>
            <h1>Criar uma nova conta</h1>
            <Form onSubmit={this.cadastro}>
                <FormGroup>
                    <FormLabel><p className = "label">Email</p></FormLabel>
                    <Form.Control  name="email" isInvalid = {errors['email']} onChange={this.handleInputChange} type="email" placeholder="Digite seu email"/>
                    <Form.Text className="text-muted">
                        Nós não vamos compartilhar nenhum de seus dados com terceiros.
                    </Form.Text>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.email}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Senha</p></FormLabel>
                    <Form.Control name="senha" isInvalid = {errors['senha']} onChange={this.handleInputChange} type="password" placeholder="Digite sua senha"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.senha}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Confirmar senha</p></FormLabel>
                    <Form.Control name="senhaCheck"  isInvalid = {errors['senhaCheck']} onChange={this.handleInputChange} type="password" placeholder="Confirme sua senha"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.senhaCheck}
                    </Form.Control.Feedback>
                </FormGroup>


                <FormGroup>
                    <FormLabel><p className = "label">Telefone</p></FormLabel>
                    <Form.Control  name="telefone" isInvalid = {errors['telefone']} onChange = {this.handleInputChange} placeholder = "083 98206-6789"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.telefone}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Cep</p></FormLabel>
                    <Form.Control name = "cep" isInvalid = {errors['cep']} onChange = {this.handleInputChange} placeholder="9999-999"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.cep}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Endereço</p></FormLabel>
                    <Form.Control name = "endereco" isInvalid = {errors['endereco']} onChange = {this.handleInputChange} placeholder="Rua bacharel irenaldo de albuquerque chaves, 201, bloco L, apt 402"/>

                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.endereco}
                    </Form.Control.Feedback>
                </FormGroup>
            <Row>
                <Col>
                    <Button type="submit" variant="warning">Cadastrar</Button>
                </Col>
            </Row>
            </Form>

        </div>
        
        );
    }
}

export default Cadastro;