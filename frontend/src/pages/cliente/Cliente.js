import React from 'react'
import LoggedNavbar from '../../components/navbarLogged/Navbar'
import {Row, Col, Button} from 'react-bootstrap'

import "./Cliente.css"

import api from "../../service/api"

import Feed from "../../components/feed/Feed"
class Cliente extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            feed : [], //Feed de buscas que o usuário tenha feito
            cliente : this.props.location.state.key //Chave recebida do cliente, ao ele fazer o login

        }


    }

    async componentDidMount() {
        const response = await api.get('posts');
        this.setState({feed : response.data});
    }

    render(){
        return (
            <div id = "Cliente">
                <LoggedNavbar/>
                <header>
                    <Row>
                        <Col><h1>Busca</h1></Col>
                        <Col><Button variant="success" href = "/newpost">Nova pesquisa de profissional</Button></Col>
                    </Row>
                </header>
                <hr/>
                {/* <section id = "post-list">
                    {this.state.feed.map(post ==> (<RequestResume title = {post.title} description = {post.description} responses = {this.responses} view = {this.view}/>))}
                </section> */}
                <Feed usuario = {this.state.cliente} tipoUsuario = "cliente" tipoFeed = "buscas"/>
            </div>
        );
    }
}

export default Cliente