import React from 'react'
import {Link} from 'react-router-dom'

//Componentes bootstrap
import Button from 'react-bootstrap/Button';
import Form from "react-bootstrap/Form";
import logo from "../assets/beakIcon.svg";

import "./login.css"
class TelaInicial extends React.Component {
    render() {
      return (
        <div className = "login">
            <Link to = '/'>
            <img className = "logo" src = {logo} alt = "Logo beak"/>
            </Link>

            <Form inline>
            <Form.Group controlId="formBasicEmail">
                <Form.Label>Email</Form.Label>
                <Form.Control type="email" placeholder="Email" />
            </Form.Group>
            <Form.Group controlId="formBasicPassword">
                <Form.Label>Senha</Form.Label>
                <Form.Control type="password" placeholder="Senha" />
            </Form.Group>
            <Form.Group controlId="formBasicChecbox">
                <Form.Check type="checkbox" label="Check me out" />
            </Form.Group>
            <Button variant="warning" type="submit">
                Login
            </Button>
            </Form>
        </div>
      );
    }
  }

export default TelaInicial