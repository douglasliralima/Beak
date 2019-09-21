import React from "react"
import "./Cadastro.css"
import {Form, FormLabel, FormGroup, FormText, Row, Col} from "react-bootstrap"

class Cadastro extends React.Component {
    render(){
        return (
        <div id = "Cadastro">
            <h1>Criar uma nova conta</h1>
            <Form>
                {/* <FormGroup>
                    <FormLabel column sm="2"><p className = "label">Email</p></FormLabel>
                    <Col>
                    <Form.Control type="email" placeholder="Digite seu email" />
                    <Form.Text className="text-muted">
                        Nós não vamos compartilhar nenhum de seus dados com terceiros.
                    </Form.Text>
                    </Col>
                </FormGroup> */}

                <FormGroup>
                    <FormLabel><p className = "label">Email</p></FormLabel>
                    <Form.Control type="email" placeholder="Digite seu email" />
                    <Form.Text className="text-muted">
                        Nós não vamos compartilhar nenhum de seus dados com terceiros.
                    </Form.Text>
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Senha</p></FormLabel>
                    <Form.Control type="password" placeholder="Digite sua senha" />
                </FormGroup>

                <FormGroup>
                    <FormLabel><p className = "label">Confirmar senha</p></FormLabel>
                    <Form.Control type="password" placeholder="Confirme sua senha"/>
                </FormGroup>


                <FormGroup>
                    <FormLabel><p className = "label">Telefone</p></FormLabel>
                    <Form.Control/>
                </FormGroup>


                <FormGroup as = {Row}>
                    <Col>
                        <FormLabel><p className = "label">Cep</p></FormLabel>
                        <Form.Control placeholder="9999-999" />
                    </Col>

                    <Col>
                        <FormLabel><p className = "label">Cidade</p></FormLabel>
                        <Form.Control />
                    </Col>
                </FormGroup>

                <FormGroup as = {Row}>
                    <Col>
                        <FormLabel><p className = "label">Bairro</p></FormLabel>
                        <Form.Control />
                    </Col>

                    <Col>
                        <FormLabel><p className = "label">Complemento</p></FormLabel>
                        <Form.Control />
                    </Col>
                </FormGroup>
            </Form>
        </div>
        
        );
    }
}

export default Cadastro;