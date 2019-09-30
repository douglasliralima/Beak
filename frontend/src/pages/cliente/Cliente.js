import React from 'react'
import LoggedNavbar from '../../components/navbarLogged/Navbar'
import {Row, Col, Button} from 'react-bootstrap'
import {BrowserRouter, Route, Link, NavLink, Redirect, Prompt} from 'react-router-dom';

import "./Cliente.css"

import api from "../../service/api"

import Feed from "../../components/feed/Feed"
class Cliente extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            feed : [], //Feed de buscas que o usuário tenha feito
            cliente : this.props.location.state.key, //Chave recebida do cliente, ao ele fazer o login
            novabusca : false //Boolean com a intenção do usuário em criar ou não uma nova busca
        }


    }

    // async componentDidMount() {
    //     const response = await api.get('posts');
    //     this.setState({feed : response.data});
    // }
    handleNovaBusca = (e) => {
        let {novabusca} = this.state;
        novabusca = true
        this.setState({novabusca : novabusca})
        window.location.reload()
    }

    render(){
        return (
            <div id = "Cliente">
            <BrowserRouter>
                <LoggedNavbar/>
                <header>
                    <Row>
                        <Col><h1>Busca</h1></Col>
                        <Col><Button variant="success" onClick = {this.handleNovaBusca}>Nova pesquisa de profissional</Button></Col>
                        {this.state.novabusca && <Redirect to= {{pathname : '/cliente/novabusca', state : {key : this.state.cliente}}}/>}
                    </Row>
                </header>
                <hr/>
                {/* <section id = "post-list">
                    {this.state.feed.map(post ==> (<RequestResume title = {post.title} description = {post.description} responses = {this.responses} view = {this.view}/>))}
                </section> */}
                <Feed usuario = {this.state.cliente} tipoUsuario = "cliente" tipoFeed = "buscas"/>
            </BrowserRouter>
            </div>
        );
    }
}

export default Cliente