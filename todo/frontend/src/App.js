import React from 'react';
import axios from 'axios';

import './App.css';
import UserList from './components/User.js'
import HeaderList from './components/Header.js'
import FooterList from './components/Footer.js'
import ProjectList from './components/Project.js'
import TODOList from './components/TODO.js'
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            'users': [],
            'projects': [],
            'TODOs': [],
            'token': ''
       }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        //localStorage.setItem('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
    this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        //const token = localStorage.setItem(key, 'token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
            axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,password: password})
        .then(response => {
            console.log(response.data)
        }).catch(error => alert('Неверный логин или пароль'))
        }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
    if (this.is_authenticated())
    {
        headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
    }

    load_data(){

        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data
                    this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/TODOs', {headers})
            .then(response => {
                const TODOs = response.data
                    this.setState(
                    {
                        'TODOs': TODOs
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()

    }



    render () {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/TODOs'>TODOs</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button
                        onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                        <Switch>
                            <Route exact path='/' component={() => <UserList items={this.state.users} />} />
                            <Route exact path='/projects' component={() => <ProjectList items={this.state.items} />} />
                            <Route exact path='/TODOs' component={() => <TODOList items={this.state.items} />} />
                            <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />

                            <Route component={NotFound404}/>
                        </Switch>
                </BrowserRouter>
                <HeaderList headers={this.state.header} />
                <FooterList footers={this.state.footer} />
        </div>
        )
    }
}
export default App;







