import React from 'react'
//import {Link} from 'react-router-dom'

//Componentes bootstrap
import Button from 'react-bootstrap/Button';
//import Form from "react-bootstrap/Form";
//import logo from "../assets/beakIcon.svg";
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import Carousel from "react-bootstrap/Carousel"


import howWork1 from '../assets/howWork1.png';
import howWork2 from '../assets/howWork2.png';
import howWork3 from '../assets/howWork3.png';
import arrow from "../assets/yellowArrow-right.png";
import assistenciaEletrodomestico from "../assets/assistenciaEletrodomestico.jpg"
import servicosDomesticos from "../assets/servicosDomesticos.jpg"
import construcaoCivil from "../assets/construcaoCivil.jpg"
import reformaReparos from "../assets/reformaReparos.jpg"
import instalacaoEletrica from "../assets/instalacaoEletrica.jpg"
import assistenciaInformatica from "../assets/assistenciaInformatica.jpeg"
import servicosEncanamento from "../assets/servicosEncanamento.jpg"

import "./TelaInicial.css";
class TelaInicial extends React.Component {
    render() {
      return (
        <div id = "telaInicial">

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
              <Carousel>
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    src="holder.js/800x400?text=First slide&bg=373940"
                    alt="First slide"
                  />
                  <Carousel.Caption>
                    <h3>First slide label</h3>
                    <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                  </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    src="holder.js/800x400?text=Second slide&bg=282c34"
                    alt="Third slide"
                  />

                  <Carousel.Caption>
                    <h3>Second slide label</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                  </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                  <img
                    className="d-block w-100"
                    src="holder.js/800x400?text=Third slide&bg=20232a"
                    alt="Third slide"
                  />

                  <Carousel.Caption>
                    <h3>Third slide label</h3>
                    <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                  </Carousel.Caption>
                </Carousel.Item>
              </Carousel>
            </Col>
          </Row>
          <Row>
            <h1 class = "section-title">Como funciona?</h1>
          </Row>
          <Row>
          <Col>
            <div class = "how-work">
              <img src = {howWork1}/>
              <p class = "short-description">
                Publique gratuitamente o serviço
              </p>
            </div>
          </Col>
          <Col>
            <img class = "arrow" src = {arrow}/>
          </Col>
          <Col>
            <div class = "how-work">
              <img src = {howWork2}/>
              <p class = "short-description">
                Receba respostas rápidas.
              </p>
            </div>
            </Col>
            <Col>
              <img class = "arrow" src = {arrow}/>
            </Col>
            <Col>
            <div class = "how-work">
              <img src = {howWork3}/>
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

            <div class = "categoria">
            <a href = "#">
                <img src = {assistenciaEletrodomestico} class = "category-img"/>

                <p class = "short-description">
                  Assistência Eletrodomésticos
                </p>

                <p class = "anuncio">
                Anuncie Aqui
                </p>
              </a>
            </div>
            <div class = "categoria">
              <img src = {servicosDomesticos} class = "category-img"/>

              <p class = "short-description">
                Serviços domésticos
              </p>

              <p class = "anuncio">
              Anuncie Aqui
              </p>

            </div>
            <div class = "categoria">
              <img src = {construcaoCivil} class = "category-img"/>

              <p class = "short-description">
                Construção Civil
              </p>

              <p class = "anuncio">
              Anuncie Aqui
              </p>
              
            </div>
            <div class = "categoria">
              <img src = {reformaReparos} class = "category-img"/>

              <p class = "short-description">
              Reformas e Reparos
              </p>

              <p class = "anuncio">
              Anuncie Aqui
              </p>
            </div>
            <div class = "categoria">
              <img src = {instalacaoEletrica} class = "category-img"/>

              <p  class = "short-description">
              Instalação Elétrica
              </p>

              <p class = "anuncio">
              Anuncie Aqui
              </p>            
            </div>
            <div class = "categoria">
              <img src = {assistenciaInformatica} class = "category-img"/>

              <p class = "short-description">
              Assistência de Informática
              </p>

              <p class = "anuncio">
              Anuncie Aqui
              </p>           

            </div>
            <div class = "categoria">
              <img src = {servicosEncanamento} class = "category-img"/>

              <p class = "short-description">
              Encanamento
              </p>

              <p class = "anuncio">
              Anuncie Aqui
              </p>            
            </div>
          </Row>
        </Container>
        
        </div>
      );
    }
  }

export default TelaInicial