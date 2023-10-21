import "./ConferencesList.css";
import React from "react";
import { Link } from "react-router-dom";

function ConferenceItem({ conference }) {
  return (
    <div className="conference-item">
      <img src={conference.image_url} alt={conference.title} />
      <h3>{conference.title}</h3>
      <p>Venue: {conference.venue}</p>
      <p>Date: {new Date(conference.date_time).toLocaleDateString()}</p>
      <p>By: {conference.creator.full_name}</p>
      <Link to={`/conference/${conference.id}`} className="more-info-btn">
        More Info
      </Link>
    </div>
  );
}

function ConferencesList({ conferences }) {
  return (
    <div className="conferences-list">
      {conferences.map((conference) => (
        <ConferenceItem key={conference.id} conference={conference} />
      ))}
    </div>
  );
}

export default ConferencesList;
