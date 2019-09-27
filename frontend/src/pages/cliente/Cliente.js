import React from 'react'
import LoggedNavbar from '../../components/navbarLogged/Navbar'
import {Container, Row, Col, Button} from 'react-bootstrap'

import "./Cliente.css"
class Cliente extends React.Component {
    render(){
        return (
            <div id = "Cliente">
                <LoggedNavbar/>
                <Row>
                    <Col><h1>Busca</h1></Col>
                    <Col><Button variant="success">Nova pesquisa de profissional</Button></Col>
                </Row>
                <hr/>
            </div>
        );
    }
}

export default Cliente