import sqlite3
from SQLite_Database import SQLiteDatabase

DATABASE_NAME = 'Total_Life_DB'

# --- Clinician Table ---

CLINICIAN_TABLE_NAME = 'clinican_table'

#COLUMN    =        column_name         column_type     column_key
NPI_COLUMN =        'npi_id'+ ' ' +     'INTEGER'+ ' ' +   'PRIMARY KEY'
FIRST_NAME_COLUMN = 'first_name'+ ' ' + 'TEXT'
LAST_NAME_COLUMN =  'last_name'+ ' ' +  'TEXT'
STATE_COLUMN =      'state'+ ' ' +      'TEXT'

CLINICIAN_TABLE = NPI_COLUMN +', '+ FIRST_NAME_COLUMN +', '+ LAST_NAME_COLUMN +', '+ STATE_COLUMN

# --- Patient Table ---

PATIENT_TABLE_NAME = 'patient_table'

#COLUMN    =        column_name                     column_type         column_key
PATIENT_ID_COLUMN = 'patient_id'+ ' ' +             'INTEGER'+ ' ' +   'PRIMARY KEY'
FIRST_NAME_COLUMN = 'first_name'+ ' ' +             'TEXT'
LAST_NAME_COLUMN =  'last_name'+ ' ' +              'TEXT'
PHONE_COLUMN =      'phone_number'+ ' ' +           'TEXT'
CLINICIAN_COLUMN =  'npi_id'+ ' ' +                 'INTEGER'+ ' '+     f'REFERENCES {CLINICIAN_TABLE_NAME} (npi_id)'

PATIENT_TABLE = PATIENT_ID_COLUMN +', '+ FIRST_NAME_COLUMN +', '+ LAST_NAME_COLUMN +', '+ PHONE_COLUMN +', '+ CLINICIAN_COLUMN

# --- Appointment Table ---

APPOINTMENT_TABLE_NAME = 'appointment_table'

#COLUMN    =            column_name              column_type        column_key
APPIONTMENT_ID_COLUMN = 'appointment_id'+ ' ' + 'INTEGER'+ ' ' +    'PRIMARY KEY'
PATIENT_COLUMN =        'patient_id'+ ' ' +     'INTEGER'+ ' '+     f'REFERENCES {PATIENT_TABLE_NAME} (patient_id)'
CLINICIAN_COLUMN =      'npi_id'+ ' ' +         'INTEGER'+ ' '+     f'REFERENCES {CLINICIAN_TABLE_NAME} (npi_id)'
DATE_TIME_COLUMN =      'date_time'+ ' ' +      'TEXT'
STATUS_COLUMN =         'status'+ ' ' +         'TEXT'

APPIONTMENT_TABLE = APPIONTMENT_ID_COLUMN  +', '+ DATE_TIME_COLUMN +', '+ STATUS_COLUMN +', '+ PATIENT_COLUMN +', '+ CLINICIAN_COLUMN 


# --- Creating/Editing Database Object ---
#Creating the database <<DATABASE_NAME>> 
active_database = SQLiteDatabase(DATABASE_NAME)

#Creates clinician, patient and appointment tables
active_database.create_table(CLINICIAN_TABLE_NAME,CLINICIAN_TABLE)
active_database.create_table(PATIENT_TABLE_NAME,PATIENT_TABLE)
active_database.create_table(APPOINTMENT_TABLE_NAME,APPIONTMENT_TABLE)

#Adding 'dummy' data to Database
active_database.add_entity(CLINICIAN_TABLE_NAME,"'npi_id','first_name', 'last_name', 'state'","'1','John', 'Doe', 'AB'")
active_database.add_entity(PATIENT_TABLE_NAME,"'patient_id','first_name', 'last_name', 'phone_number','npi_id'","'1','Jane', 'Smith', '555-4125','1'")
active_database.add_entity(APPOINTMENT_TABLE_NAME,"'appointment_id','patient_id', 'npi_id', 'date_time','status'","'1','1', '1', '15:00 1/1/25','Booked'")



#Closing the database
active_database.close_database()
