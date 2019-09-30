import React from "react"
import {Form, FormLabel, FormGroup, Row, Col, Button} from "react-bootstrap";
import {BrowserRouter, Redirect} from "react-router-dom"
import NavBar from "../../components/navbarLogged/Navbar"
import "./NovaBusca.css"

import api from "../../service/api"

class NewPost extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            cliente : this.props.location.state.key, //Cliente que está fazendo aquela busca
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
            if (res == "Busca cadastrada") {
                alert("Sua busca foi cadastrada!");
                this.setState({
                    formSubmitted: true
                })
                window.location.reload()
            }
        }).catch(function(err){
            console.error(err);
            // window.location.reload()
        });
    }

    render(){
        let {formSubmitted, cliente} = this.state;
        return (
        <div id = "Busca">
            <BrowserRouter>
                {/* <NavBar/> */}
                <h1>Criar uma nova busca</h1>
                <Form onSubmit={this.busca}>
                    <FormGroup>
                        <FormLabel><p className = "label">Nome</p></FormLabel>
                        <Form.Control  name="titulo" onChange={this.handleInputChange} placeholder = "Digite o titulo"/>
                    </FormGroup>

                    <FormGroup>
                        <FormLabel><p className = "label">Categoria</p></FormLabel>
                        <Form.Control  name="categoria" onChange={this.handleInputChange} placeholder = "Digite a categoria"/>
                    </FormGroup>

                    <FormGroup>
                        <FormLabel><p className = "label">Descricao Geral</p></FormLabel>
                        <Form.Control  name="descricaoGeral" onChange={this.handleInputChange} placeholder = "Digite a Descricao Geral"/>
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