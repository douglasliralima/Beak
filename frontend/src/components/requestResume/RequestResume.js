import React from 'react'
import {Col, Row} from 'react-bootstrap'
import resumeIcon from "./resumeIcon.png"

import "./RequestResume.css"
class RequestResume extends React.Component{
    /**
     * props:
     * title - Titulo da postagem,
     * description - descrição da postagem,
     * responses - orçamentos de resposta para aquela postagem,
     * view - Visualizações até então daquela postagem,
     */
    render (){
        return (
            <div class = "RequestResume">
                <Row>
                    <Col sm  = {2} className = "icon-section">
                        <img class = "iconDescription" src = {resumeIcon}/>
                    </Col>
                    <Col>
                        <h1 id = "title">{this.props.title}</h1>
                        <p>{this.props.description}</p>
                    </Col>
                    <Col sm  = {2}>
                        <p>orçamentos : {this.props.responses}</p>
                        <p>visualizações : {this.props.view}</p>
                    </Col>
                </Row>
                <hr/>
            </div>
        );
    }
}

export default RequestResume