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
PATIENT_ID_COLUMN =        'patient_id'+ ' ' +             'INTEGER'+ ' ' +   'PRIMARY KEY'
FIRST_NAME_COLUMN = 'first_name'+ ' ' +             'TEXT'
LAST_NAME_COLUMN =  'last_name'+ ' ' +              'TEXT'
PHONE_COLUMN =      'phone_number'+ ' ' +           'TEXT'
CLINICIAN_COLUMN =  'preferred_clinician_id'+ ' ' + 'TEXT'+ ', ' +       f'FOREIGN KEY (preferred_clinician_id) REFERENCES {CLINICIAN_TABLE_NAME} (npi_id)'

PATIENT_TABLE = PATIENT_ID_COLUMN +', '+ FIRST_NAME_COLUMN +', '+ LAST_NAME_COLUMN +', '+ PHONE_COLUMN +', '+ CLINICIAN_COLUMN


# --- Creating/Editing Database Object ---
#Creating the database <<DATABASE_NAME>> 
active_database = SQLiteDatabase(DATABASE_NAME)

#Creates clinician and patient tables
active_database.create_table(CLINICIAN_TABLE_NAME,CLINICIAN_TABLE)
active_database.create_table(PATIENT_TABLE_NAME,PATIENT_TABLE)

#Closing the database
active_database.close_database()
