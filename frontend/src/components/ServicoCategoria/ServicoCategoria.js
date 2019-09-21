import React from 'react'

import "./ServicoCategoria.css"

class CategoriaServico extends React.Component{
    render(){
      return(
        <div class = "categoria">
          <a href = "#">
              <img src = {this.props.img} class = "category-img" alt = {this.props.categoria}/>
  
              <p class = "short-description">
                {this.props.categoria}
              </p>
  
              <p class = "anuncio">
              Anuncie Aqui
              </p>
            </a>
          </div>
      );
    }
}

export default CategoriaServico;