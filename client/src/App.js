import './App.css';
import Footer from './components/Footer';
import Header from './components/Header';
import Login from './components/Login';
import SignUp from './components/SignUp';
import {Route, Switch, Redirect} from 'react-router-dom'
import Todo from './components/Todo';

function App() {
  return (
    <div className="App">
      <Header/>
      <Switch>
        <Route exact path="/">
          <Redirect to= '/login'/>
        </Route>
        <Route path="/signup">
          <SignUp />
        </Route>
        <Route path="/login">
          <Login/>
        </Route>
        <Route path="/todo">
          <Todo/>
        </Route>
      </Switch>
      <Footer/>
    </div>
  );
}

export default App;
