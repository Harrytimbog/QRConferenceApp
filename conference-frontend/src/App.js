import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import ConferenceDetail from "./pages/ConferenceDetail";
import EditConference from "./pages/EditConference";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/" element={Home} />
        <Route path="/login" element={Login} />
        <Route path="/signup" element={SignUp} />
        <Route path="/conference/:id" element={ConferenceDetail} />
        <Route path="/edit-conference/:id" element={EditConference} />
      </Routes>
    </Router>
  );
}

export default App;
