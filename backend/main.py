from SQLite_Database import SQLiteDatabase
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Basic get response
@app.route('/appointments', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def appointments_endpoints():
    arguments = {
        "appointment_id": request.args.get('appointment_id'),
        "appt_patient_id": request.args.get('appt_patient_id'),
        "appt_clinician_id": request.args.get('appt_clinician_id'),
        "date_time": request.args.get('date_time'),
        "status": request.args.get('status'),
        "start_date": request.args.get('start_date'),  # Added start date
        "end_date": request.args.get('end_date')  # Added end date
    }

    # Open database
    DATABASE_NAME = 'Total_Life_DB'
    active_database = SQLiteDatabase(DATABASE_NAME)
    table_name = 'appointment_table'

    if request.method == 'GET':
        # Read the correct data based on query parameters
        query_conditions = []
        if arguments['start_date'] and arguments['end_date']:
            # Handle date range condition
            try:
                start_date = datetime.strptime(arguments['start_date'], '%Y-%m-%dT%H:%M')  # Assuming input is datetime-local format
                end_date = datetime.strptime(arguments['end_date'], '%Y-%m-%dT%H:%M')
                query_conditions.append(f"date_time BETWEEN '{start_date}' AND '{end_date}'")
            except ValueError:
                return jsonify({"error": "Invalid date format, please use YYYY-MM-DDTHH:MM for start_date and end_date"}), 400
        
        # Add other query conditions based on the provided parameters
        for argument, value in arguments.items():
            if value and argument not in ['start_date', 'end_date']:  # Skip date range arguments here
                query_conditions.append(f"{argument} = '{value}'")

        query_condition = ' AND '.join(query_conditions) if query_conditions else '1=1'  # Default to '1=1' to get all records if no filters are provided
        
        FOREIGN_KEY_CONDITION = f'INNER JOIN patient_table ON appointment_table."appt_patient_id" = patient_table."patient_id"'
        select = "appointment_id, date_time,status,appt_patient_id,appt_clinician_id,patient_first_name,patient_last_name"
        
        returned_results = active_database.search_table(select, table_name, query_condition, 'date_time ASC', None, FOREIGN_KEY_CONDITION)

     
        # Format the returned results into a list of dictionaries
        returned_entities = []
        if returned_results:
            for result in returned_results:
                returned_entities.append({
                    "appointment_id": result[0],
                    "date_time": result[1],
                    "status": result[2],
                    "appt_patient_id": result[3],
                    "appt_clinician_id": result[4],
                    "appt_patient_first_name":result[5],
                    "appt_patient_last_name":result[6],

                })

        returned_entites = returned_entities

    elif request.method == 'POST':
        # Create new entity in appointments table
        active_database.add_entity(table_name, "'appt_patient_id', 'appt_clinician_id', 'date_time', 'status'", 
                                    f"'{arguments['appt_patient_id']}', '{arguments['appt_clinician_id']}', '{arguments['date_time']}', '{arguments['status']}'")
        returned_entites = 'Added'

    elif request.method == 'PATCH':
        # Update entity in appointments table
        for argument in arguments:
            if arguments[argument]:
                active_database.update_entity(table_name, f"{argument} = '{arguments[argument]}'", 
                                              f"appointment_id = {arguments['appointment_id']}")
        
        returned_entites = 'Updated'

    elif request.method == 'DELETE':
        # Delete entity in appointments table
        active_database.delete_entity(table_name, f"appointment_id = {arguments['appointment_id']}")
        returned_entites = 'Deleted'

    # Closing the database
    active_database.close_database()

    return jsonify(returned_entites)


# Running app
if __name__ == '__main__':
    app.run(debug=True)