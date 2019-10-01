import React from "react"

import RequestResume from "../requestResume/RequestResume"
import api from "../../service/api"



class Feed extends React.Component {
    /**
     * 
     * @param props.usuario A chave correspondente a quem está pedindo para renderizar seu feed
     * @param props.tipoUsuario A string com o tipo do usuário (cliente|profissional)
     * @param props.tipoFeed Qual o feed que está se desejando (pendente|andamento|finalizado)
     */

    constructor(props){
        super(props);

        this.state = {
            posts : [],
        }
    }

    async componentDidMount(){
        if(this.props.tipoUsuario == "cliente"){
            switch(this.props.tipoFeed){
                case "pendente":
                    const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                    // console.log(response)
                    this.setState({ posts : response.data});
                // case "andamento":
                //     const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                //     // console.log(response)
                //     this.setState({ posts : response.data});
                // case "finalizado":
                //     const response = await api.get('/servico-cliente', {params : {key : this.props.usuario}})
                //     // console.log(response)
                //     this.setState({ posts : response.data});
            }

        }
        else if (this.props.tipoUsuario == "profissional"){

        }
       
    }

    render(){
        return (
            <div id = "post-list">
                {this.state.posts.map(post => (
                    <RequestResume title = {post.title} description = {post.description} responses = "2" view = "2"/>
                ))}
            </div>
        )
    }
}

export default Feed