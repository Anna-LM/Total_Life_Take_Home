from SQLite_Database import SQLiteDatabase
from flask import Flask, request, jsonify
import time
import json


from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


from datetime import datetime

#Basic get response
@app.route('/appointments', methods=['GET','POST','PATCH','DELETE'])
def appointments_endpoints():
    appointment_id = request.args.get('appointment_id')
    appt_patient_id = request.args.get('appt_patient_id')
    appt_clinician_id = request.args.get('appt_clinician_id')
    date_time = request.args.get('date_time')
    status = request.args.get('status')

    #open database <<DATABASE_NAME>>
    DATABASE_NAME = 'Total_Life_DB'
    active_database = SQLiteDatabase(DATABASE_NAME)
    table_name = 'appointment_table'

    if request.method == 'GET':
        #Read the correct data
        returned_entites = active_database.search_table('*',table_name,f'appointment_id = {appointment_id}','date_time DESC',None, None)
        print(returned_entites[0])

        returned_entites = {
            "appointment_id": returned_entites[0][0],
            "appt_patient_id": returned_entites[0][1],
            "appt_clinician_id": returned_entites[0][2],
            "date_time": returned_entites[0][3],
            }
        

    elif request.method == 'POST':
        #create new entity in appointments table
        active_database.add_entity(table_name,"'appt_patient_id', 'appt_clinician_id', 'date_time','status'",f"'{appt_patient_id}', '{appt_clinician_id}', '{date_time}','{status}'")
        returned_entites = 'Added'

    elif request.method == 'PATCH':
        #Update entity in appointments table
        active_database.update_entity(table_name,f"date_time = '{date_time}'",f'appointment_id = {appointment_id}')
        returned_entites = 'Updated'

    elif request.method == 'DELETE':
        #Delete entity in appointments table
        active_database.delete_entity(table_name,f"appointment_id = {appointment_id}")
        returned_entites = 'Deleted'


    #Closing the database
    active_database.close_database()

    return jsonify(returned_entites)
    
    
# Running app
if __name__ == '__main__':
    app.run(debug=True)
