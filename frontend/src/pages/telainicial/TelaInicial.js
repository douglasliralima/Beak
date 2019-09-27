import React from 'react'
//import {Link} from 'react-router-dom'

//Componentes bootstrap
import Button from 'react-bootstrap/Button';
//import Form from "react-bootstrap/Form";
//import logo from "../assets/beakIcon.svg";
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

//Description Imagens
import descriptionImage from '../../assets/descriptionImage.png';

//Explicação Imagens
import howWork1 from '../../assets/howWork1.png';
import howWork2 from '../../assets/howWork2.png';
import howWork3 from '../../assets/howWork3.png';
import arrow from "../../assets/yellowArrow-right.png";


//Categorias imagens
import assistenciaEletrodomestico from "../../assets/assistenciaEletrodomestico.jpg"
import servicosDomesticos from "../../assets/servicosDomesticos.jpg"
import construcaoCivil from "../../assets/construcaoCivil.jpg"
import reformaReparos from "../../assets/reformaReparos.jpg"
import instalacaoEletrica from "../../assets/instalacaoEletrica.jpg"
import assistenciaInformatica from "../../assets/assistenciaInformatica.jpeg"
import servicosEncanamento from "../../assets/servicosEncanamento.jpg"

import "./TelaInicial.css";

import ServicoCategoria from "../../components/servicoCategoria/ServicoCategoria.js"
import NavBar from "../../components/navbarUnlogged/navbar.js"

class TelaInicial extends React.Component {
    render() {
      return (
        <div id = "telaInicial">
        <NavBar/>
        <Container>
          <Row>
            <Col>
              <h1>
                Encontre os melhores profissionais perto de você!
              </h1>
              <p>
                Descreve aquilo que precisa em poucos cliques, sem sair de casa. Clique abaixo e faça um orçamento.
              </p>
              <Button variant="success">Encontrar Profissional</Button>
            </Col>
            <Col>
              <img
                className="d-block w-100"
                src= {descriptionImage}
                alt="First slide"
                id = "description-image"
              />
            </Col>
          </Row>  
          <Row>
            <h1 class = "section-title">Como funciona?</h1>
          </Row>
          <Row>
          <Col>
            <div class = "how-work">
              <img src = {howWork1} alt = "Publique gratuitamente o serviço"/>
              <p class = "short-description">
                Publique gratuitamente o serviço.
              </p>
            </div>
          </Col>
          <Col>
            <img class = "arrow" src = {arrow} alt = "Proximo"/>
          </Col>
          <Col>
            <div class = "how-work">
              <img src = {howWork2} alt = "Receba respostas rápidas"/>
              <p class = "short-description">
                Receba respostas rápidas.
              </p>
            </div>
            </Col>
            <Col>
              <img class = "arrow" src = {arrow} alt = "Proximo"/>
            </Col>
            <Col>
            <div class = "how-work">
              <img src = {howWork3} alt = "Selecione o profissional que mais te atrai"/>
              <p class = "short-description">
                Selecione o profissional que mais te atrai
              </p>
            </div>
            </Col>
          </Row>
          <Row>
            <h1 class = "section-title">categorias de serviço</h1>
          </Row>
          <Row>
            <ServicoCategoria img = {assistenciaEletrodomestico} categoria = "Reparo Eletrodomesticos"/>
            <ServicoCategoria img = {servicosDomesticos} categoria = "Servicos Domesticos"/>
            <ServicoCategoria img = {construcaoCivil} categoria = "Construcao Civil"/>
            <ServicoCategoria img = {reformaReparos} categoria = "Reparo e Carpintaria"/>
            <ServicoCategoria img = {instalacaoEletrica} categoria = "Instalacao Eletrica"/>
            <ServicoCategoria img = {assistenciaInformatica} categoria = "Assistencia Informatica"/>
            <ServicoCategoria img = {servicosEncanamento} categoria = "Servicos Encanamento"/>
          </Row>
        </Container>
        
        </div>
      );
    }
  }

export default TelaInicial