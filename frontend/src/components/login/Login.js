import React, { Component } from "react";
import { Row, Form, FormGroup, FormControl, FormLabel, Button} from 'react-bootstrap';
import './login.css';
import { isEmail, isEmpty, isLength, isContainWhiteSpace } from '../../shared/validator';

class Login extends Component {

    constructor(props) {
        super(props)

        this.state = {
            formData: {}, // Contains login form data
            errors: {}, // Contains login field errors
            errorEmail: false, // Contain if email has error or not
            errorPassword: false, // Contain if password has error or not
            formSubmitted: false, // Indicates submit status of login form
            loading: false // Indicates in progress state of login form
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

    validateLoginForm = (e) => {

        let errors = {};
        let errorEmail, errorPassword = false;
        const { formData } = this.state;

        if (isEmpty(formData.email)) {
            errors.email = "Email can't be blank";
            errorEmail = true;
        } else if (!isEmail(formData.email)) {
            errors.email = "Please enter a valid email";
            errorEmail = true;
        }

        if (isEmpty(formData.password)) {
            errors.password = "Password can't be blank";
            errorPassword = true;
        }  else if (isContainWhiteSpace(formData.password)) {
            errors.password = "Password should not contain white spaces";
            errorPassword = true;
        } else if (!isLength(formData.password, { gte: 6, lte: 16, trim: true })) {
            errors.password = "Password's length must between 6 to 16";
            errorPassword = true;
        }

        this.setState({
            errorEmail : errorEmail,
            errorPassword : errorPassword,
        });

        if (isEmpty(errors)) {
            return true;
        } else {
            return errors;
        }
    }


    login = (e) => {

        e.preventDefault();

        let errors = this.validateLoginForm();
        console.log(errors);
        if(errors === true){
            alert("You are successfully signed in...");
            window.location.reload()
        } else {
            this.setState({
                errors: errors,
                formSubmitted: true
            });
        }
    }

    render() {

        const { errors, errorEmail, errorPassword } = this.state;

        return (
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
                        <FormGroup controlId="password">
                            <FormLabel>Senha</FormLabel>
                            <FormControl isInvalid = {errorPassword} type="password" name="password" placeholder="Digite sua senha" onChange={this.handleInputChange} />
                            <Form.Control.Feedback type="invalid">
                                {errors.password}
                            </Form.Control.Feedback>
                        </FormGroup>
                    </Form>
                </Row>
                <Row>
                    <div id = "option-login">
                        <a href = "/cadastro">Não possuo conta</a>
                        <Button type="submit" variant="warning">Entrar</Button>
                    </div>
                </Row>
            </div>
        )
    }
}

export default Login;