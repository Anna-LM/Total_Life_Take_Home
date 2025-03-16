import React, { useState } from 'react';

const App = () => {
  const [appointmentDetails, setAppointmentDetails] = useState(null);
  const [appointmentsByClinician, setAppointmentsByClinician] = useState([]);
  const [appointmentsByPatient, setAppointmentsByPatient] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const [appointmentId, setAppointmentId] = useState('');
  const [clinicianName, setClinicianName] = useState('');
  const [patientName, setPatientName] = useState('');

  // Date Range for Searching
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  // New appointment form data
  const [newAppointmentId, setNewAppointmentId] = useState('');
  const [newPatientID, setNewPatientID] = useState('');
  const [newClinicianID, setNewClinicianID] = useState('');
  const [newDate, setNewDate] = useState('');
  const [newStatus, setNewStatus] = useState('Scheduled');

  // Delete appointment form data
  const [deleteAppointmentId, setDeleteAppointmentId] = useState('');

  // Update appointment form data
  const [updateAppointmentId, setUpdateAppointmentId] = useState('');
  const [updatePatientID, setUpdatePatientID] = useState('');
  const [updateClinicianID, setUpdateClinicianID] = useState('');
  const [updateDate, setUpdateDate] = useState('');
  const [updateStatus, setUpdateStatus] = useState('Scheduled');

  // Fetch appointment by ID
  const fetchAppointment = async () => {
    if (!appointmentId) {
      setError('Please enter an appointment ID');
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?appointment_id=${appointmentId}`);
      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setAppointmentsByClinician(Array.isArray(data) ? data : [data]); // Ensure it's always an array
      setError(null);
    } catch (err) {
      console.error('Error fetching appointments:', err);
      setError(err.message);
      setAppointmentsByClinician([]); // Reset appointments if error occurs
    }
    setLoading(false);
  };

  // Fetch appointments by clinician name
  const fetchAppointmentsByClinician = async () => {
    if (!clinicianName) {
      setError('Please enter a clinician name');
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?appt_clinician_id=${clinicianName}`);
      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setAppointmentsByClinician(Array.isArray(data) ? data : [data]); // Ensure it's always an array
      setError(null);
    } catch (err) {
      console.error('Error fetching appointments:', err);
      setError(err.message);
      setAppointmentsByClinician([]); // Reset appointments if error occurs
    }
    setLoading(false);
  };

  // Fetch appointments by patient name
  const fetchAppointmentsByPatient = async () => {
    if (!patientName) {
      setError('Please enter a patient name');
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?appt_patient_id=${patientName}`);
      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setAppointmentsByClinician(Array.isArray(data) ? data : [data]); // Ensure it's always an array
      setError(null);
    } catch (err) {
      console.error('Error fetching appointments:', err);
      setError(err.message);
      setAppointmentsByClinician([]); // Reset appointments if error occurs
    }
    setLoading(false);
  };

  // Fetch appointments by date range
  const fetchAppointmentsByDate = async () => {
    if (!startDate || !endDate) {
      setError('Please enter both start and end dates');
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?start_date=${startDate}&end_date=${endDate}`);
      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setAppointmentsByClinician(Array.isArray(data) ? data : [data]); // Ensure it's always an array
      setError(null);
    } catch (err) {
      console.error('Error fetching appointments:', err);
      setError(err.message);
      setAppointmentsByClinician([]); // Reset appointments if error occurs
    }
    setLoading(false);
  };

  // Create a new appointment (POST request)
  const createAppointment = async () => {
    if (!newPatientID || !newClinicianID || !newDate) {
      setError('Please fill in all fields for the new appointment');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?appt_patient_id=${newPatientID}&appt_clinician_id=${newClinicianID}&date_time=${newDate}&status=${newStatus}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setError(null);
      alert('Appointment created successfully');
      // Clear the form after successful creation
      setNewAppointmentId('');
      setNewPatientID('');
      setNewClinicianID('');
      setNewDate('');
      setNewStatus('Scheduled');
    } catch (err) {
      console.error('Error creating appointment:', err);
      setError(err.message);
    }
    setLoading(false);
  };

  // Update an appointment (PATCH request)
  const updateAppointment = async () => {
    if (!updateAppointmentId) {
      setError('Please fill in appointment ID to update');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?appointment_id=${updateAppointmentId}&appt_patient_id=${updatePatientID}&appt_clinician_id=${updateClinicianID}&date_time=${updateDate}&status=${updateStatus}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setError(null);
      alert('Appointment updated successfully');
      // Clear the form after successful update
      setUpdateAppointmentId('');
      setUpdatePatientID('');
      setUpdateClinicianID('');
      setUpdateDate('');
      setUpdateStatus('Scheduled');
    } catch (err) {
      console.error('Error updating appointment:', err);
      setError(err.message);
    }
    setLoading(false);
  };

  // Delete an appointment (POST request)
  const deleteAppointment = async () => {
    if (!deleteAppointmentId) {
      setError('Please fill in all fields to delete appointment');
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/appointments?appointment_id=${deleteAppointmentId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!res.ok) throw new Error('Network response was not ok');
      const data = await res.json();
      setError(null);
      alert('Appointment deleted successfully');
      // Clear the form after successful creation
      setDeleteAppointmentId('');
    } catch (err) {
      console.error('Error deleting appointment:', err);
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Search Appointments</h1>

      {/* Search by Appointment ID */}
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

      {/* Search by Clinician */}
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

      {/* Search by Patient */}
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

      {/* Search by Date Range */}
      <div className="flex gap-2 mb-4">
        <input
          type="datetime-local"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="datetime-local"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          className="border p-2 rounded"
        />
        <button
          onClick={fetchAppointmentsByDate}
          className="bg-orange-500 text-white px-4 py-2 rounded"
        >
          Search by Date Range
        </button>
      </div>

      {/* Error Message */}
      {error && <p className="text-red-500">{error}</p>}

      {/* Loading State */}
      {loading && <p>Loading...</p>}

      {/* Display Appointments */}
      {appointmentsByClinician.length > 0 && (
        <div className="mt-4">
          <h2 className="font-bold">Appointments</h2>
          {appointmentsByClinician.map((appt) => (
            <div key={appt.appointment_id} className="p-4 border rounded bg-gray-100 mb-2">
              <p>Appointment ID: {appt.appointment_id}</p>
              <p>Patient: {appt.appt_patient_id}</p>
              <p>Clinician: {appt.appt_clinician_id}</p>
              <p>Date: {new Date(appt.date_time).toLocaleString()}</p>
              <p>Status: {appt.status}</p>
              <p> -------- </p>
            </div>
          ))}
        </div>
      )}

      {/* Add New Appointment Form */}
      <div className="mt-4">
        <h2 className="font-bold">Create New Appointment</h2>
        <div className="flex gap-2 mb-4">
          <input
            type="text"
            value={newPatientID}
            onChange={(e) => setNewPatientID(e.target.value)}
            placeholder="Patient ID"
            className="border p-2 rounded"
          />
          <input
            type="text"
            value={newClinicianID}
            onChange={(e) => setNewClinicianID(e.target.value)}
            placeholder="Clinician ID"
            className="border p-2 rounded"
          />
          <input
            type="datetime-local"
            value={newDate}
            onChange={(e) => setNewDate(e.target.value)}
            className="border p-2 rounded"
          />
          <select
            value={newStatus}
            onChange={(e) => setNewStatus(e.target.value)}
            className="border p-2 rounded"
          >
            <option value="Scheduled">Scheduled</option>
            <option value="Completed">Completed</option>
            <option value="Cancelled">Cancelled</option>
          </select>
          <button
            onClick={createAppointment}
            className="bg-blue-500 text-white px-4 py-2 rounded"
          >
            Create Appointment
          </button>
        </div>
      </div>
      
      {/* Update Appointment Form */}
      <div className="mt-4">
        <h2 className="font-bold">Update Appointment</h2>
        <div className="flex gap-2 mb-4">
          <input
            type="text"
            value={updateAppointmentId}
            onChange={(e) => setUpdateAppointmentId(e.target.value)}
            placeholder="Appointment ID"
            className="border p-2 rounded"
          />
          <input
            type="text"
            value={updatePatientID}
            onChange={(e) => setUpdatePatientID(e.target.value)}
            placeholder="Patient ID"
            className="border p-2 rounded"
          />
          <input
            type="text"
            value={updateClinicianID}
            onChange={(e) => setUpdateClinicianID(e.target.value)}
            placeholder="Clinician ID"
            className="border p-2 rounded"
          />
          <input
            type="datetime-local"
            value={updateDate}
            onChange={(e) => setUpdateDate(e.target.value)}
            className="border p-2 rounded"
          />
          <select
            value={updateStatus}
            onChange={(e) => setUpdateStatus(e.target.value)}
            className="border p-2 rounded"
          >
            <option value="Scheduled">Scheduled</option>
            <option value="Completed">Completed</option>
            <option value="Cancelled">Cancelled</option>
          </select>
          <button
            onClick={updateAppointment}
            className="bg-green-500 text-white px-4 py-2 rounded"
          >
            Update Appointment
          </button>
        </div>
      </div>

      {/* Delete Appointment Form */}
      <div className="mt-4">
        <h2 className="font-bold">Delete Appointment</h2>
        <div className="flex gap-2 mb-4">
          <input
            type="text"
            value={deleteAppointmentId}
            onChange={(e) => setDeleteAppointmentId(e.target.value)}
            placeholder="Appointment ID"
            className="border p-2 rounded"
          />
          <button
            onClick={deleteAppointment}
            className="bg-red-500 text-white px-4 py-2 rounded"
          >
            Delete Appointment
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
