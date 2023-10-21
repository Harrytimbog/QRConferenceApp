import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Container, Box, Typography, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
const BASEURL = "https://947b-92-26-6-164.ngrok-free.app";

const ConferenceDetail = () => {
  const [conference, setConference] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const { conferenceId } = useParams();
  console.log(conferenceId);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchConference = async () => {
      try {
        const response = await fetch(`${BASEURL}/conferences/${conferenceId}`);
        const data = await response.json();

        console.log(data);

        if (response.ok) {
          setConference(data);
        } else {
          setError(data.message || "Failed to fetch conference details");
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchConference();
  }, [conferenceId]);

  const handleDelete = async () => {
    try {
      const response = await fetch(`${BASEURL}/conferences/${conferenceId}`, {
        method: "DELETE",
      });

      if (response.ok) {
        navigate("/");
      } else {
        const data = await response.json();
        setError(data.message || "Failed to delete conference");
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <Container>
      <Box sx={{ mt: 6, mb: 3 }}>
        {loading ? (
          <Typography>Loading...</Typography>
        ) : error ? (
          <Typography color="error">{error}</Typography>
        ) : (
          <>
            <Typography variant="h4" component="h1" gutterBottom>
              {conference.title}
            </Typography>
            {/* Display the conference image if available */}
            {conference.image_url && (
              <Box sx={{ my: 2 }}>
                <img
                  src={conference.image_url}
                  alt={conference.title}
                  style={{ maxWidth: "100%", height: "auto" }}
                />
              </Box>
            )}
            <Typography variant="h6" gutterBottom>
              Date: {conference.date}
            </Typography>
            <Typography variant="body1" gutterBottom>
              {conference.description}
            </Typography>

            {/* Show Edit & Delete buttons for creators or admins */}
            {/* You can adjust this check according to your logic */}
            {conference.isCreatorOrAdmin && (
              <Box mt={3}>
                <Button
                  variant="contained"
                  color="primary"
                  style={{ marginRight: "15px" }}
                  onClick={() => {
                    // Redirect to edit conference page
                    navigate(`${BASEURL}/edit-conference/${conferenceId}`);
                  }}
                >
                  Edit
                </Button>
                <Button
                  variant="contained"
                  color="secondary"
                  onClick={handleDelete}
                >
                  Delete
                </Button>
              </Box>
            )}
          </>
        )}
      </Box>
    </Container>
  );
};

export default ConferenceDetail;
