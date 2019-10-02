import React from 'react'
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";
import {BrowserRouter, Redirect} from "react-router-dom"

import "./PostDescription.css"

/**
 * @param 
 */
class PostDescription extends React.Component{
    /**
     * 
     * @param props.usuario A chave correspondente a quem está pedindo para renderizar seu feed
     * @param props.tipoUsuario A string com o tipo do usuário (cliente|profissional)
     * @param props.postagem O identificador daquela postagem
     */

    constructor(props){
        super(props)
        let campos = ["titulo", "categoria", "descricaoGeral"]
        let aux = {}
        for (let i in campos) {
            aux[campos[i]] = false
        }
        this.state = {
            usuario : "profissional",


            errors : aux, //Booleans se cada campo está invalido
            errorsDescription : [], //Descrição do erro que aconteceu naquele campo
            formData : {categoria : "Servicos Domesticos"}, //Dados a respeito do busca
            formSubmitted : false, //Boolean que diz se a busca foi ou não realizado
        };
    }

    render(){
        let {errors, errorsDescription, formSubmitted, cliente} = this.state;

        return(
            <div id = "post-description">
                <BrowserRouter>
                    {/* <NavBar/> */}
                    <h1>Descrição do pedido</h1>
                    <p className  = "titulo">Nome</p>
                    <p className = "description">Limpeza da casa nos finais de semana</p>
                    <p className  = "titulo">Categoria</p>
                    <p className = "description">Servicos Domesticos</p>
                    <p className  = "titulo">Descricao Geral</p>
                    <p className = "description">Gostaria de alguém que pudesse vir a minha casa para dar uma limpeza geral na louça.</p>

                    <h1>Orçamentos</h1>
                    <hr/>

                    <Row className = "justify-content-center">
                        <Button type="submit" variant="success">Fazer orçamentos</Button>
                    </Row>


                    <Form onSubmit={this.busca}>
                    <Row className = "justify-content-center">

                        <Col>
                            <FormGroup >
                                <FormLabel><p className = "titulo">Apresentação</p></FormLabel>
                                <Form.Control name="apresentacao" isInvalid = {errors['apresentacao']} onChange={this.handleInputChange} placeholder = "Breve descrição do motivo para te contratar"/>
                                <Form.Control.Feedback type="invalid">
                                    {errorsDescription.apresentacao}
                                </Form.Control.Feedback>
                            </FormGroup>
                        </Col>
                        
                        <Col sm = {2}>
                            <FormGroup >
                                <FormLabel><p className = "titulo">Valor</p></FormLabel>
                                <Form.Control name="valor" isInvalid = {errors['valor']} onChange={this.handleInputChange} placeholder = "Digite o valor"/>
                                <Form.Control.Feedback type="invalid">
                                    {errorsDescription.valor}
                                </Form.Control.Feedback>
                            </FormGroup>
                        </Col>

                        <Col sm = {2}>
                            <FormLabel><p className = "titulo">Tipo</p></FormLabel>
                            <Form.Control name="categoria" onChange={this.handleInputChange} placeholder = "Digite a categoria" as = "select">
                                <option></option>
                                <option>Por Serviço</option>
                                <option>Por Hora</option>
                            </Form.Control>
                        </Col>
                    </Row>
                    <Row className = "justify-content-center">
                        <Button type="submit" variant="danger">Cancelar</Button>
                        <Button type="submit" variant="success">Orçar</Button>
                    </Row>
                    </Form>
                    <hr/>

                        <Row>
                            <Col sm = {2}>
                                {/* <img className = "profissional" href = "#"> */}
                                <p className = "profssional-descricao">foto</p>
                            </Col>
                            <Col>
                                <p className = "description">Tenho grande determinação em fazer as tarefas ao qual eu me
                                comprometo a fazer e a pontualidade é uma das minhas marcas.</p>
                            </Col>
                            <Col sm = {2}>
                                <p className = "titulo">R$100/hora</p>
                            </Col>
                            <Col sm = {2}>
                                <Button type="submit" variant="success">O</Button>
                                <Button type="submit" variant="danger">X</Button>
                            </Col>
                        </Row>
                        
                </BrowserRouter>
            </div>
        );
    }
}

export default PostDescription;