import React, { useState, useEffect } from 'react';


const App = () => {
  const [appointmentDetails, setAppointmentDetails] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/appointments?appointment_id=1')
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((data) => {
        // If the API returns an array, you might need to pick the first element
        setAppointmentDetails(Array.isArray(data) ? data[0] : data);
      })
      .catch((err) => {
        console.error('Error fetching appointment:', err);
        setError(err.message);
      });
  }, []);

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Appointment Details</h1>
      {appointmentDetails ? (
        <div className="p-4 border rounded bg-gray-100">
          <p>Patient: {appointmentDetails.appointment_id}</p>
          <p>Date: {new Date(appointmentDetails.date_time).toLocaleString()}</p>
          <p>Status: {appointmentDetails.status}</p>
        </div>
      ) : (
        <p>Loading appointment details...</p>
      )}
    </div>
  );
};

export default App;