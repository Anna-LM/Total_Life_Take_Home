import React, { useState } from 'react';

const App = () => {
  const [appointmentDetails, setAppointmentDetails] = useState(null);
  const [appointmentsByClinician, setAppointmentsByClinician] = useState([]);
  const [appointmentsByPatient, setAppointmentsByPatient] = useState([]);
  const [error, setError] = useState(null);

  const [appointmentId, setAppointmentId] = useState('');
  const [clinicianName, setClinicianName] = useState('');
  const [patientName, setPatientName] = useState('');

  // Fetch appointment by ID
  const fetchAppointment = () => {
    if (!appointmentId) {
      setError('Please enter an appointment ID');
      return;
    }

    fetch(`http://127.0.0.1:5000/appointments?appointment_id=${appointmentId}`)
      .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
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

  // Fetch appointments by clinician name
  const fetchAppointmentsByClinician = () => {
    if (!clinicianName) {
      setError('Please enter a clinician name');
      return;
    }

    fetch(`http://127.0.0.1:5000/appointments?appt_clinician_id=${clinicianName}`)
    .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
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

  // Fetch appointments by patient name
  const fetchAppointmentsByPatient = () => {
    if (!patientName) {
      setError('Please enter a patient name');
      return;
    }

    fetch(`http://127.0.0.1:5000/appointments?appt_patient_id=${patientName}`)
    .then((res) => {
        if (!res.ok) throw new Error('Network response was not ok');
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
      <h1 className="text-xl font-bold mb-4">Search Appointments</h1>

      {/* Input and Button for Searching by Appointment ID */}
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
          Search by ID
        </button>
      </div>

      {/* Input and Button for Searching by Clinician */}
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={clinicianName}
          onChange={(e) => setClinicianName(e.target.value)}
          placeholder="Enter Clinician Name"
          className="border p-2 rounded"
        />
        <button
          onClick={fetchAppointmentsByClinician}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Search by Clinician
        </button>
      </div>

      {/* Input and Button for Searching by Patient */}
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={patientName}
          onChange={(e) => setPatientName(e.target.value)}
          placeholder="Enter Patient Name"
          className="border p-2 rounded"
        />
        <button
          onClick={fetchAppointmentsByPatient}
          className="bg-purple-500 text-white px-4 py-2 rounded"
        >
          Search by Patient
        </button>
      </div>

      {/* Error Message */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Display Single Appointment Details */}
      {appointmentDetails && (
        <div className="p-4 border rounded bg-gray-100">
          <h2 className="font-bold">Appointment Details</h2>
          <p>Appointment ID: {appointmentDetails.appointment_id}</p>
          <p>Patient: {appointmentDetails.appt_patient_id}</p>
          <p>Clinician: {appointmentDetails.appt_clinician_id}</p>
          <p>Date: {new Date(appointmentDetails.date_time).toLocaleString()}</p>
          <p>Status: {appointmentDetails.status}</p>
        </div>
      )}
    </div>
  );
};

export default App;