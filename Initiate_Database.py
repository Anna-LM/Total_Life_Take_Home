import sqlite3
from SQLite_Database import SQLiteDatabase

DATABASE_NAME = 'Total_Life_DB'

# --- Clinician Table ---

CLINICIAN_TABLE_NAME = 'clinican_table'

#COLUMN    =        column_name         column_type     column_key
NPI_COLUMN =        'npi_id'+ ' ' +     'TEXT'+ ' ' +   'PRIMARY KEY'
FIRST_NAME_COLUMN = 'first_name'+ ' ' + 'TEXT'
LAST_NAME_COLUMN =  'last_name'+ ' ' +  'TEXT'
STATE_COLUMN =      'state'+ ' ' +      'TEXT'

CLINICIAN_TABLE = NPI_COLUMN +', '+ FIRST_NAME_COLUMN +', '+ LAST_NAME_COLUMN +', '+ STATE_COLUMN


# --- Creating/Editing Database Object ---
#Creating the database <<DATABASE_NAME>> 
active_database = SQLiteDatabase(DATABASE_NAME)

#Create a table of preset cities with at least city_id and city_name
active_database.create_table(CLINICIAN_TABLE_NAME,CLINICIAN_TABLE)

#Closing the database
active_database.close_database()
