import React from 'react'
import {Switch, Route} from 'react-router-dom';

import TelaInicial from './pages/telainicial/TelaInicial';
import login from './pages/login/Login.js';
import cadastro from './pages/cadastro/Cadastro'
import cliente from './pages/cliente/Cliente';
import NewPost from "./pages/newpost/NewPost"
//import New from './pages/New';

/**
 * O react router dom, para fazer as rotas rec  ebe tbm um JSX, veja que precisamos do
 * switch envelopando essas duas rotas, isso acontece, pois o react-router-dom olha se
 * o url que o usuário digitou, contem uma dessas rotas e monta os componentes em 
 * sequência.
 * Colocamos o switch para que ele selecione uma dessas rotas e usamos o parametro 
 * exact para que não caia sempre na rota raiz nesse switch.
 */
function Routes(){
    return (
        <Switch>
            <Route path = '/' exact component = {TelaInicial} />
            <Route path = '/login' exact component = {login} />
            <Route path = '/cadastro' exact component = {cadastro} />
            <Route path = '/cliente' exact component = {cliente} />
            <Route path = "/newpost" exact component = {NewPost} />
        </Switch>
    );
}

export default Routes