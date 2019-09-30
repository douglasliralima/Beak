import React from "react"

import RequestResume from "../requestResume/RequestResume"
import api from "../../service/api"

/**
 * 
 * @param props.usuario A chave correspondente a quem está pedindo para renderizar seu feed
 * @param props.tipoUsuario A string com o tipo do usuário (cliente|profissional)
 * @param props.tipoFeed Qual o feed que está se desejando (buscas|andamento|finalizado)
 */
function Feed(props){
    {/* <section id = "post-list">
        {this.state.feed.map(post ==> (<RequestResume title = {post.title} description = {post.description} responses = {this.responses} view = {this.view}/>))}
    </section> 
        <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>
    */}

    return (
        <div id = "#feed">
            <h1>Olá {props.usuario}, do tipo {props.tipoUsuario}, querendo feed de {props.tipoFeed}</h1>
            <RequestResume title = "Limpeza de louça nos finais de semana" description = "Gostaria de alguém que pudesse vir a minha casa esse final de semana para dar uma limpeza geral na casa, incluindo os banheiros" responses = "2" view = "2"/>
        </div>
        );
}

export default Feed