import React from "react"
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";

import RequestResume from "../requestResume/RequestResume"
import api from "../../service/api"



class Feed extends React.Component {
    /**
     * 
     * @param props.usuario A chave correspondente a quem está pedindo para renderizar seu feed
     * @param props.tipoUsuario A string com o tipo do usuário (cliente|profissional)
     * @param props.tipoFeed Qual o feed que está se desejando (pendente|andamento|finalizado)
     */

    constructor(props){
        super(props);

        this.state = {
            posts : [],
            categoria : "",
        }
    }

    HandleCategoriaChange = (event) => {
        const target = event.target;
        const name = target.name;
        const value = target.value;

        let {categoria} = this.state;

        categoria = value;

        this.setState({
            categoria : categoria,
        });
    }

    async componentDidMount(){
        if(this.props.tipoUsuario == "cliente"){
            switch(this.props.tipoFeed){
                case "pendente":
                    const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                    // console.log(response)
                    this.setState({ posts : response.data});
                // case "andamento":
                //     const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                //     // console.log(response)
                //     this.setState({ posts : response.data});
                // case "finalizado":
                //     const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                //     // console.log(response)
                //     this.setState({ posts : response.data});
            }
        }
        else if (this.props.tipoUsuario == "profissional"){
            switch(this.props.tipoFeed){
                case "pendente":
                    const response = await api.get('/servico-profissional', {params : {key : this.props.usuario, categoria :  this.props.categoria}})
                    // console.log(response)
                    this.setState({ posts : response.data});
                // case "andamento":
                //     const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                //     // console.log(response)
                //     this.setState({ posts : response.data});
                // case "finalizado":
                //     const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                //     // console.log(response)
                //     this.setState({ posts : response.data});
            }
        }
    }

    render(){
        return (
            <div id = "post-list">
                {this.state.categoria === "profissional" &&
                    (<FormGroup>
                        <FormLabel><p className = "label">Categoria de serviço:</p></FormLabel>
                        <Form.Control  name="categoria" onChange={this.HandleCategoriaChange} placeholder = "Digite a categoria" as = "select">
                            <option></option>
                            <option>Servicos Domesticos</option>
                            <option>Reparo Eletrodomesticos</option>
                            <option>Construcao Civil</option>
                            <option>Reparo e Carpintaria</option>
                            <option>Instalacao Eletrica</option>
                            <option>Assistencia Informatica</option>
                            <option>Servicos Encanamento</option>
                        </Form.Control>
                    </FormGroup>)}
                {this.state.posts.map(post => (
                    <RequestResume title = {post.title} description = {post.description} responses = "2" view = "2"/>
                ))}
            </div>
        )
    }
}

export default Feed