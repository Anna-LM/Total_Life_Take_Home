from SQLite_Database import SQLiteDatabase
from flask import Flask, request

app = Flask(__name__)

#Basic get response
@app.route('/appointments', methods=['GET'])#,'POST'])
def return_appointments():
    return "ABC", 200 
    
app.run()


