import React from "react"
import {Navbar, Nav, NavDropdown} from "react-bootstrap"
import "./Navbar.css"

function BootstrapNavbar(){
    return (
        <Navbar collapseOnSelect expand="lg" variant="light">
            <Navbar.Brand >Beak</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                <Nav.Link className = "tela" href="#buscas">Buscas</Nav.Link>
                <Nav.Link className = "tela" href="#andamento">Em andamento</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default BootstrapNavbar