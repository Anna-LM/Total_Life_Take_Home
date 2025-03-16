import React, { useState } from 'react';

const App = () => {
  const [appointmentDetails, setAppointmentDetails] = useState(null);
  const [error, setError] = useState(null);
  const [appointmentId, setAppointmentId] = useState('');

  const fetchAppointment = () => {
    if (!appointmentId) {
      setError('Please enter an appointment ID');
      return;
    }

    fetch(`http://127.0.0.1:5000/appointments?appointment_id=${appointmentId}`)
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((data) => {
        setAppointmentDetails(Array.isArray(data) ? data[0] : data);
        setError(null);
      })
      .catch((err) => {
        console.error('Error fetching appointment:', err);
        setError(err.message);
        setAppointmentDetails(null);
      });
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Search Appointment</h1>
      
      {/* Input and Button for Searching */}
      <div className="flex gap-2 mb-4">
        <input
          type="number"
          value={appointmentId}
          onChange={(e) => setAppointmentId(e.target.value)}
          placeholder="Enter Appointment ID"
          className="border p-2 rounded"
        />
        <button
          onClick={fetchAppointment}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Search
        </button>
      </div>

      {/* Error Message */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Display Appointment Details */}
      {appointmentDetails ? (
        <div className="p-4 border rounded bg-gray-100">
          <p>Patient: {appointmentDetails.patient_name}</p>
          <p>Date: {new Date(appointmentDetails.date_time).toLocaleString()}</p>
          <p>Status: {appointmentDetails.status}</p>
        </div>
      ) : (
        !error && <p>Enter an appointment ID to search.</p>
      )}
    </div>
  );
};

export default App;