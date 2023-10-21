import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import ConferenceDetail from "./pages/ConferenceDetail";
import EditConference from "./pages/EditConference";
import Navbar from "./pages/components/Navbar";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route
          path="/conference/:conferenceId"
          element={<ConferenceDetail />}
        />
        <Route path="/edit-conference/:id" element={<EditConference />} />
      </Routes>
    </Router>
  );
}

export default App;
