import React, { useState, useEffect } from "react";
import ConferencesList from "./components/ConferencesList";
import fakeData from "../data/fake-data.json";
import "./Home.css";

function Home() {
  // const [conferences, setConferences] = useState(fakeData);
  const [conferences, setConferences] = useState([]);
  // const [loading, setLoading] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // fetch("https://localhost:5000/conferences")
    fetch("/conferences")
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
