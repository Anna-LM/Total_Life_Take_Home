from SQLite_Database import SQLiteDatabase
from flask import Flask, request, jsonify

app = Flask(__name__)

#Basic get response
@app.route('/appointments', methods=['GET','POST'])
def return_appointments():
    appointment_id = request.args.get('appointment_id')
    appt_patient_id = request.args.get('appt_patient_id')
    appt_clinician_id = request.args.get('appt_clinician_id')
    date_time = request.args.get('date_time')
    status = request.args.get('status')

    #open database <<DATABASE_NAME>>
    DATABASE_NAME = 'Total_Life_DB'
    active_database = SQLiteDatabase(DATABASE_NAME)

    if request.method == 'GET':
        #Read the correct data
        returned_entites = active_database.search_table('*','appointment_table',f'appointment_id = {appointment_id}','date_time DESC',None, None)
    
    elif request.method == 'POST':
        #create new entity in appointments table
        active_database.add_entity('appointment_table',"'appt_patient_id', 'appt_clinician_id', 'date_time','status'",f"'{appt_patient_id}', '{appt_clinician_id}', '{date_time}','{status}'")
        returned_entites = 'Added'


    #Closing the database
    active_database.close_database()

    return jsonify(returned_entites), 200 
    
app.run()


