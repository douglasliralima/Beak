import React from "react";
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";

import {isEmpty} from '../../shared/validator';
import api from "../../service/api"

// import NavBar from "../../components/navbarUnlogged/navbar.js"
import "./Cadastro.css";

class Cadastro extends React.Component {
    constructor(props){
        super(props);
        let campos = ["email", "senha", "senhaCheck", "cep", "city", "neighborhood", "complement"]
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


     async validateCadastroForm(event){
        let {formData} = this.state;
        //Retorna quais campos deram erro
        //se retornar um json vazio, todos os campos estavam corretos e o cadastro foi realizado
        let errorsDescription = await api.post("newcadastro", formData)
        let errors = {};
        console.log("ErrorDescription: " + errorsDescription)
        if (isEmpty(errorsDescription)) {
            return true;
        } else {
            for (let error in errorsDescription) {
                errors[error] = true;
            }
            this.setState({
                errors : errors,
                errorsDescription : errorsDescription,
            })
            return false;
        }
    }

    cadastro = (e) => {
        console.log("Olá, como vai vc?")

        e.preventDefault();

        let errors = this.validateCadastroForm(e);
        console.log(errors);
        if(errors === true){
            alert("You are successfully signed in...");
            // window.location.reload()
        } else {
            this.setState({
                formSubmitted: true
            });
            console.log(this.state)
        }
    }

    render(){
        const {errors, errorsDescription} = this.state;
        return (
        <div id = "Cadastro">
        
            <h1>Criar uma nova conta</h1>
            <Form onSubmit={this.cadastro}>
                <FormGroup >
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
                    <Form.Control  name="telefone" isInvalid = {errors['telefone']} onChange = {this.handleInputChange}/>
                    <Form.Control.Feedback type="invalid">
                        {errorsDescription.telefone}
                    </Form.Control.Feedback>
                </FormGroup>

                <FormGroup as = {Row}>
                    <Col>
                        <FormLabel><p className = "label">Cep</p></FormLabel>
                        <Form.Control name = "cep" isInvalid = {errors['cep']} onChange = {this.handleInputChange} placeholder="9999-999"/>
                        <Form.Control.Feedback type="invalid">
                            {errorsDescription.cep}
                        </Form.Control.Feedback>
                </Col>

                    <Col>
                        <FormLabel><p className = "label">Cidade</p></FormLabel>
                        <Form.Control name = "city" isInvalid = {errors['city']} onChange = {this.handleInputChange}/>
                        <Form.Control.Feedback type="invalid">
                            {errorsDescription.city}
                        </Form.Control.Feedback>
                    </Col>
                </FormGroup>

                <FormGroup as = {Row}>
                    <Col>
                        <FormLabel><p className = "label">Bairro</p></FormLabel>
                        <Form.Control name = "neighborhood" isInvalid = {errors['neighborhood']} onChange = {this.handleInputChange}/>
                        <Form.Control.Feedback type="invalid">
                            {errorsDescription.neighborhood}
                        </Form.Control.Feedback>
                    </Col>

                    <Col>
                        <FormLabel><p className = "label">Complemento</p></FormLabel>
                        <Form.Control name = "complement" isInvalid = {errors['complement']} onChange = {this.handleInputChange}/>
                        <Form.Control.Feedback type="invalid">
                            {errorsDescription.complement}
                        </Form.Control.Feedback>
                    </Col>
                </FormGroup>
            <Row>
                <Button type="submit" variant="warning">Cadastrar</Button>
            </Row>
            </Form>

        </div>
        
        );
    }
}

export default Cadastro;