import React, { useState } from "react";
import Navbar from "./components/shared/Navbar";
import Home from "./components/Home";
import About from "./components/About";
import Contact from "./components/Contact";
import Projects from "./components/Projects";
import Blog from "./components/blog/Blog";
import MobileNavbar from "./components/shared/MobileNavbar";

function App() {
  const [nav, setNav] = React.useState(<Home />);
  const [openMenu, setOpenMenu] = React.useState(false);
  
  function menuToggle() {
    setOpenMenu((openMenu) => !openMenu);
  }

  function handleOutsideNavClick(event){
    if(event.target.id !== 'hamburger' && event.target.id !== 'mobile-nav'){
      setOpenMenu(false)
    }
  }

  const navigate = (navigate) => {
    setOpenMenu((openMenu) => !openMenu)
    switch (navigate) {
      case "home":
        setNav(<Home />);
        break;
      case "about":
        setNav(<About />);
        break;
      case "contact":
        setNav(<Contact />);
        break;
      case "projects":
        setNav(<Projects />);
        break;
      case "blog":
        setNav(<Blog />);
        break;
      default:
        setNav(<Home />);
        break;
    }
  };

  return (
    <div className="App" onClick={handleOutsideNavClick}>
      <div className="logo" onClick={() => navigate("home")}>
        Ypper.se
      </div>
      <div
        id="hamburger"
        className={openMenu ? "hamburger hamburger-on" : "hamburger"}
        onClick={() => menuToggle()}
      >
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div
        id="mobile-nav"
        className="mobile-nav-bar"
        style={{ width: openMenu ? "250px" : "0"  }}
      >
        <MobileNavbar navigateHandler={navigate} />
      </div>
      <div className="nav-bar">
        <Navbar navigateHandler={navigate} />
      </div>
      <div className="content">{nav}</div>
    </div>
  );
}

export default App;
