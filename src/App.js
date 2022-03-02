import React from "react";
import Navbar from "./components/shared/Navbar";
import Home from './components/Home'
import About from './components/About'
import Contact from './components/Contact'
import Projects from './components/Projects'

function App() {
  const [nav, setNav] = React.useState(<Home />)

  const navigate = (navigate) => {
    switch (navigate) {
      case 'home':
        setNav(<Home />)
        break;
      case 'about':
        setNav(<About />)
        break;
      case 'contact':
        setNav(<Contact />)
        break;
      case 'projects':
        setNav(<Projects />)
        break;
      default:
        setNav(<Home />)
        break;
    }
  }

  return (
    <div className="App">
      <div>
        <Navbar navigateHandler={navigate} />
      </div>
      <div className="content">
        {nav}
      </div>
    </div>
  );
}

export default App;
