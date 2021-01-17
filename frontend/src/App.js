import Map from './Map'
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Navbar, Nav } from 'react-bootstrap';
import logo from './logo.png';



function App() {
  return (
    <Router>
      <div>
        <Navbar bg="dark" variant="dark">
          <Navbar.Brand><img className="logo" src={logo}/></Navbar.Brand>
          <Navbar.Brand>BumpMap</Navbar.Brand>
          <Nav className="mr-auto">
          </Nav>
        </Navbar>

        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/">
            <Map />
          </Route>
        </Switch>
      </div>
    </Router>
  )
}

export default App;
