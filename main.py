from SQLite_Database import SQLiteDatabase
from flask import Flask, request, jsonify

app = Flask(__name__)

#Basic get response
@app.route('/appointments', methods=['GET'])
def return_appointments():
    appointment_id = request.args.get('appointment_id')

    #open database <<DATABASE_NAME>>
    DATABASE_NAME = 'Total_Life_DB'
    active_database = SQLiteDatabase(DATABASE_NAME)

    #Read the correct data
    returned_entites = active_database.search_table('*','appointment_table',f'appointment_id = {appointment_id}','date_time DESC',None, None)
    
    #Closing the database
    active_database.close_database()

    return jsonify(returned_entites), 200 
    
app.run()


