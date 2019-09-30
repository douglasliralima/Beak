import React, { Component } from "react";
import { Row, Form, FormGroup, FormControl, FormLabel, Button} from 'react-bootstrap';
import {BrowserRouter, Route, Link, NavLink, Redirect, Prompt} from 'react-router-dom';

import { isEmail, isEmpty, isLength, isContainWhiteSpace } from '../../shared/validator';
import './login.css';
import api from "../../service/api"

class Login extends Component {

    constructor(props) {
        super(props)

        this.state = {
            formData: {}, // Contains login form data
            errors: {}, // Contains login field errors
            errorEmail: false, // Contain if email has error or not
            errorPassword: false, // Contain if senha has error or not
            formSubmitted: false, // Indicates submit status of login form
            loading: false, // Indicates in progress state of login form
            validation : false,
            key : undefined,
        }
    }

    handleInputChange = (event) => {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        let { formData } = this.state;
        formData[name] = value;

        this.setState({
            formData: formData
        });
    }

    async loginForm (e) {
        let errorDescription = {};
        let errorType = {errorEmail : false, errorPassword : false}
        // let error.errorEmail, error.errorPassword = false;
        const { formData } = this.state;

        if (isEmpty(formData.email)) {
            errorDescription.email = "Email não pode estar vazio";
            errorType.errorEmail = true;
        } else if (!isEmail(formData.email)) {
            errorDescription.email = "Por favor, entre um email valido";
            errorType.errorEmail = true;
        }

        if (isEmpty(formData.senha)) {
            errorDescription.senha = "Senha não pode estar vazia";
            errorType.errorPassword = true;
        }  else if (isContainWhiteSpace(formData.senha)) {
            errorDescription.senha = "Senha não pode conter espaços em branco";
            errorType.errorPassword = true;
        } else if (!isLength(formData.senha, { gte: 5, lte: 16})) {
            errorDescription.senha = "Sua senha deve estar entre 5 a 16 digitos";
            errorType.errorPassword = true;
        }

        if (isEmpty(errorDescription)) {
            //A requisição retorna um validation = true e a chave daquele cliente
            return await api.post('/login', formData, 
            { headers: { 'Content-Type': 'application/json' } })
            .then(function (res) {
                if(res.data.validation == false){
                    res.data.errorDescription = {email : "" , senha : ""};
                    res.data.errorType = errorType
                    alert("Email ou senha não cadastrado");
                    return res.data
                }
                else {
                    return res.data
                }
            })
            .catch(function (err) {
                alert("Falha na conexão com servidor");
                window.location.reload()
                console.error(err);
                return err
            });
        } else {
            console.log("Mandou isso")
            return {validation : false, errorDescription : errorDescription, errorType : errorType};
        }
    }


    login = (e) => {
        e.preventDefault();

        this.loginForm(e).then((validacao) =>{
            console.log(validacao);
            if(validacao.validation === true){
                alert("You are successfully signed in...");
                this.setState({
                    validation: validacao.validation,
                    key: validacao.key,
                });
                window.location.reload()
            } else {
                this.setState({
                    errorEmail : validacao.errorType.errorEmail,
                    errorPassword : validacao.errorType.errorPassword,
                    errors: validacao.errorDescription,
                    formSubmitted: true,
                });
            }
        }).catch((err) => {
            console.error(err);
        });
    }

    render() {

        const {errors, errorEmail, errorPassword, validation, key} = this.state;

        return (
            <BrowserRouter>
                <div id="login">
                    <h1 id = "logo">Beak</h1>
                    <h1>Login</h1>
                    <Row>
                        <Form onSubmit={this.login}>
                            <FormGroup controlId="email">
                                <FormLabel>Email</FormLabel>
                                <FormControl isInvalid = {errorEmail} type="text" name="email" placeholder="Digite seu email" onChange={this.handleInputChange} />
                                <Form.Control.Feedback type="invalid">
                                    {errors.email}
                                </Form.Control.Feedback>
                            </FormGroup>
                            <FormGroup controlId="senha">
                                <FormLabel>Senha</FormLabel>
                                <FormControl isInvalid = {errorPassword} type="senha" name="senha" placeholder="Digite sua senha" onChange={this.handleInputChange} />
                                <Form.Control.Feedback type="invalid">
                                    {errors.senha}
                                </Form.Control.Feedback>
                            </FormGroup>
                            <div id = "option-login">
                                <a href = "/cadastro">Não possuo conta</a>
                                <Button type="submit" variant="warning">Entrar</Button>
                            </div>
                        </Form>
                    </Row>
                    <div id = "redirect">
                        {validation && <Redirect to= {{pathname : '/cliente', state : {key : key}}} />}
                    </div>
                </div>
            </BrowserRouter>
        )
    }
}

export default Login;