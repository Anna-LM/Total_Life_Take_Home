import sqlite3
from SQLite_Database import SQLiteDatabase
from Validating_NPI import Validate_NPI

DATABASE_NAME = 'Total_Life_DB'

# --- Clinician Table ---

CLINICIAN_TABLE_NAME = 'clinican_table'

#COLUMN    =        column_name         column_type     column_key
NPI_COLUMN =        'npi_id'+ ' ' +     'INTEGER'+ ' ' +   'PRIMARY KEY'
FIRST_NAME_COLUMN = 'clinician_first_name'+ ' ' + 'TEXT'
LAST_NAME_COLUMN =  'clinician_last_name'+ ' ' +  'TEXT'
STATE_COLUMN =      'state'+ ' ' +      'TEXT'

CLINICIAN_TABLE = NPI_COLUMN +', '+ FIRST_NAME_COLUMN +', '+ LAST_NAME_COLUMN +', '+ STATE_COLUMN

# --- Patient Table ---

PATIENT_TABLE_NAME = 'patient_table'

#COLUMN    =        column_name                     column_type         column_key
PATIENT_ID_COLUMN = 'patient_id'+ ' ' +             'INTEGER'+ ' ' +   'PRIMARY KEY'
FIRST_NAME_COLUMN = 'patient_first_name'+ ' ' +             'TEXT'
LAST_NAME_COLUMN =  'patient_last_name'+ ' ' +              'TEXT'
PHONE_COLUMN =      'phone_number'+ ' ' +           'TEXT'
CLINICIAN_COLUMN =  'preferred_clinician_id'+ ' ' +                 'INTEGER'+ ' '+     f'REFERENCES {CLINICIAN_TABLE_NAME} (npi_id)'

PATIENT_TABLE = PATIENT_ID_COLUMN +', '+ FIRST_NAME_COLUMN +', '+ LAST_NAME_COLUMN +', '+ PHONE_COLUMN +', '+ CLINICIAN_COLUMN

# --- Appointment Table ---

APPOINTMENT_TABLE_NAME = 'appointment_table'

#COLUMN    =            column_name              column_type        column_key
APPIONTMENT_ID_COLUMN = 'appointment_id'+ ' ' + 'INTEGER'+ ' ' +    'PRIMARY KEY'
PATIENT_COLUMN =        'appt_patient_id'+ ' ' +     'INTEGER'+ ' '+     f'REFERENCES {PATIENT_TABLE_NAME} (patient_id)'
CLINICIAN_COLUMN =      'appt_clinician_id'+ ' ' +         'INTEGER'+ ' '+     f'REFERENCES {CLINICIAN_TABLE_NAME} (npi_id)'
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

# -- CRUD --
#Create
active_database.add_entity(PATIENT_TABLE_NAME,"'patient_id','patient_first_name', 'patient_last_name', 'phone_number','preferred_clinician_id'","'1','Jane', 'Smith', '555-4125','1'")
active_database.add_entity(APPOINTMENT_TABLE_NAME,"'appointment_id','appt_patient_id', 'appt_clinician_id', 'date_time','status'","'1','1', '1', '15:00 1/1/25','Booked'")

demo_npi_number = '1851510887'
demo_clinician_first_name = 'John'
demo_clinician_last_name = 'AAGESEN'
demo_clinician_state = 'AB'

if Validate_NPI (demo_npi_number,demo_clinician_first_name,demo_clinician_last_name,demo_clinician_state):
    print('here')
    active_database.add_entity(CLINICIAN_TABLE_NAME,"'npi_id','clinician_first_name', 'clinician_last_name', 'state'",f'"{demo_npi_number}","{demo_clinician_first_name}", "{demo_clinician_last_name}", "{demo_clinician_state}"')
else:
    print('Invalid Clinican Details')

#Read
returned = active_database.search_table('date_time,patient_first_name',APPOINTMENT_TABLE_NAME,'appt_clinician_id = 1','date_time DESC',5, f'INNER JOIN {PATIENT_TABLE_NAME} ON {APPOINTMENT_TABLE_NAME}."appt_patient_id" = {PATIENT_TABLE_NAME}."patient_id"')
print(returned)

#Update
active_database.update_entity(PATIENT_TABLE_NAME,"patient_last_name = 'Brown'",'patient_id = 1')

#Delete
active_database.delete_entity(APPOINTMENT_TABLE_NAME,"appointment_id = 1")




#Closing the database
active_database.close_database()
