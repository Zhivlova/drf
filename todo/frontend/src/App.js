import React from 'react';
import axios from 'axios';

import './App.css';
import UserList from './components/User.js'
import HeaderList from './components/Header.js'
import FooterList from './components/Footer.js'
import ProjectList from './components/Project.js'
import TODOList from './components/TODO.js'
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'


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
        const user1 = {uid: 166996564533, first_name: 'Петр', last_name: 'Васильев', email: 'p.vasilev@mail.ru'}
        const user2 = {uid: 6535796564533, first_name: 'Ирина', last_name: 'Петренко', email: 'irishka@mail.ru'}
        const users = [user1, user2]
        const project1 = {uid: 9594938534571, title: 'Ежедневник', link: 'http://127.0.0.1:8000/project1', project_users: 166996564533}
        const project2 = {uid: 9875359385571, title: 'Календарь', link: 'http://127.0.0.1:8000/project2', project_users: 6535796564533}
        const projects = [project1, project2]
        const todo1 = {uid: 124957686797891, todo_project: 9875359385571, text: 'Напоминание', create_date: '12:00 05.05.2022', update_date: '19:42 15.05.2022', todo_user: 6535796564533}
        const todo2 = {uid: 156456576867978, todo_project: 9875359385571, text: 'День рождения', create_date: '20:18 10.05.2022', update_date: '20:18 10.05.2022', todo_user: 6535796564533}
        const TODOs = [todo1, todo2]
        this.state = {
            'users': [],
            'projects': [],
            'TODOs': []
       }
    }

    /*componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                    this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }*/



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
                        </ul>
                    </nav>
                        <Switch>
                            <Route exact path='/' component={() => <UserList items={this.state.users} />} />
                            <Route exact path='/projects' component={() => <ProjectList items={this.state.items} />} />
                            <Route exact path='/TODOs' component={() => <TODOList items={this.state.items} />} />
                           <Route component={NotFound404} />
                        </Switch>
                </BrowserRouter>
                <HeaderList headers={this.state.header} />
                <FooterList footers={this.state.footer} />
            </div>
        )
    }
}
export default App;







