import React from 'react'
import LoggedNavbar from '../../components/navbarLogged/Navbar'
import {Row, Col, Button} from 'react-bootstrap'

import "./Cliente.css"

import api from "../../service/api"

import RequestResume from "../../components/requestResume/RequestResume"
class Cliente extends React.Component {
    state = {
        feed : [], //Feed de buscas que o usuário tenha feito

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
                <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>
                <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>
                <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>
                <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>
                <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>

            </div>
        );
    }
}

export default Cliente