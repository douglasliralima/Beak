import React from "react"
import { Button} from 'react-bootstrap';
import "./navbar.css"

function NavBar(){
    return (
        <div id = "navbar">
            <ul id = "help-options">
                <li><a href = "#">Como funciona?</a></li>
                <li><a href = "#">Segurança</a></li>
            </ul>
            <ul id = "user-options">
                <li><Button variant="warning" size = "lg">Cadastrar-se</Button></li>
                <li><Button variant="outline-warning" size = "lg">Entrar</Button></li>
            </ul>
            <hr/>
        </div>
    );
}

export default NavBar;