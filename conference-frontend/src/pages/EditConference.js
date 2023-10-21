import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios"; // Assuming you're using axios for HTTP requests
import { useNavigation } from "react-router-dom";
const BASEURL = "https://947b-92-26-6-164.ngrok-free.app";

function EditConference() {
  const { conferenceId } = useParams();
  const navigation = useNavigation();

  const [conferenceData, setConferenceData] = useState({
    title: "",
    description: "",
    date: "",
    // Add other conference fields here...
  });
  const [error, setError] = useState("");

  useEffect(() => {
    // Fetch the current conference data when the page loads
    axios
      .get(`${BASEURL}/conferences/${conferenceId}`)
      .then((response) => {
        setConferenceData(response.data);
      })
      .catch((err) => {
        console.error("Error fetching conference:", err);
      });
  }, [conferenceId]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setConferenceData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    axios
      .put(`/api/conferences/${conferenceId}`, conferenceData)
      .then((response) => {
        // Redirect to the conference detail page or another suitable location
        navigation.navigate(`{BASEURL}/conferences/${conferenceId}`);
      })
      .catch((err) => {
        setError("Failed to update the conference.");
        console.error(err);
      });
  };

  return (
    <div className="conference-edit-container">
      <h2>Edit Conference</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Title:</label>
          <input
            type="text"
            name="title"
            value={conferenceData.title}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Description:</label>
          <textarea
            name="description"
            value={conferenceData.description}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Date:</label>
          <input
            type="date"
            name="date"
            value={conferenceData.date}
            onChange={handleInputChange}
            required
          />
        </div>
        {/* Add more input fields for other conference details if needed */}
        <button type="submit">Update Conference</button>
      </form>
    </div>
  );
}

export default EditConference;
