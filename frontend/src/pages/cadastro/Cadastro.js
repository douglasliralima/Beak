import React from "react";
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";

// import {isEmpty} from '../../shared/validator';
import api from "../../service/api"

import NavBar from "../../components/navbarUnlogged/navbar.js"
import "./Cadastro.css";

class Cadastro extends React.Component {
    constructor(props){
        super(props);
        let campos = ["tipo", "nome", "email", "senha", "senhaCheck", "cpf", "nascimento", "telefone", "cep", "endereco"]
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

    handleTypeChange = (event) => {
        //Pegando em quem ouve uma mudança
        const target = event.target;
        const value = target.value;
        const name = target.name;
        let {formData} = this.state;

        if (value === "Publicar serviços"){
            formData[name] = "cliente"
        } else if (value === "Encontrar serviços"){
            formData[name] = "profissional"
        }else{
            formData[name] = ""
        }
        console.log(formData)
        this.setState({formData : formData});
    }


     async CadastraForm(event){
        //Pega os dados do state e define a foto
        let {formData} = this.state;
        formData['foto'] = "eu.png"

        //Tenta cadastrar o cliente e retorna a resposta do servidor
        return await api.post("cadastro-cliente", formData, 
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

    cadastro = (e) => {
        e.preventDefault();

        //Primeiro vamos mandar ao servidor os dados no formulário para ele fazer o cadastro
        //Sucesso: Mensagem que o cliente foi cadastrado em caso de sucesso
        //Falha: Mensagens de quais foram os erros
        this.CadastraForm(e)
        .then((errorsDescription) => {
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
        }).catch(function(err){
            console.error(err);
            // window.location.reload()
        });
    }

    render(){
        const {errors, errorsDescription, formData} = this.state;
        return (
        <div id = "Cadastro">
            <NavBar/>
            <h1>Criar uma nova conta</h1>
            <Form onSubmit={this.cadastro}>

                <FormGroup>
                    <FormLabel><p className = "label">O que você procura na nossa plataforma?</p></FormLabel>
                    <Form.Control  name="tipo" isInvalid = {errors['tipo']} onChange={this.handleTypeChange} as = "select">
                        <option></option>
                        <option>Publicar serviços</option>
                        <option>Encontrar serviços</option>
                    </Form.Control>
                    <Form.Text className="text-muted">
                        Nós não vamos compartilhar nenhum de seus dados com terceiros.
                    </Form.Text>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.tipo}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Nome</p></FormLabel>
                    <Form.Control  name="nome" isInvalid = {errors['nome']} onChange={this.handleInputChange} placeholder = "Digite seu nome"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.nome}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Email</p></FormLabel>
                    <Form.Control  name="email" isInvalid = {errors['email']} onChange={this.handleInputChange} type="email" placeholder="Digite seu email"/>
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
                    <FormLabel><p className = "label">Cpf</p></FormLabel>
                    <Form.Control  name="cpf" isInvalid = {errors['cpf']} onChange={this.handleInputChange} placeholder = "065.124.381-71"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.cpf}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Data de nascimento</p></FormLabel>
                    <Form.Control  name="nascimento" isInvalid = {errors['nascimento']} onChange={this.handleInputChange} placeholder = "065.124.381-71"/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.nascimento}
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