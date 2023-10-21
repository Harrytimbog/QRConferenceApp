import React, { useState, useEffect } from "react";
import ConferencesList from "./components/ConferencesList";
// import fakeData from "../data/fake-data.json";
import "./Home.css";

function Home() {
  // const [conferences, setConferences] = useState(fakeData);
  const [conferences, setConferences] = useState([]);
  // const [loading, setLoading] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  // const BASE_URL = process.env.REACT_APP_API_BASE_URL;
  const BASEURL = "https://947b-92-26-6-164.ngrok-free.app";
  console.log(BASEURL);

  useEffect(() => {
    fetch(`${BASEURL}/conferences`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setConferences(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading conferences: {error.message}</p>;

  return (
    <div>
      <h2>Upcoming Conferences</h2>
      <ConferencesList conferences={conferences} />
    </div>
  );
}

export default Home;
