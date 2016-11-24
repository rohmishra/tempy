# SETUP Keys and database
# (c) 2016. Rohan Mishra
import os
import sqlite3
from sys import argv
import io

# TODO: Add support for arguments
script, arg = argv

# Create Weather Database. Does not request or return any value.
# Create TABLE wtr SCHEMA
# CREATE TABLE wtr (geoTag text, FriendlyName text, lid number, wether object)
# DB UNUSED
def createHistDB():
    dbConnect=sqlite3.connect('hist.db')
    cnt = dbConnect.cursor()
    cnt.execute('''CREATE TABLE wtr (geoTag text, FriendlyName text, lid number, wether object)''')
    cnt.execute('''Insert INTO wtr VALUES ('18.9219841,72.8346543', 'South Bombay, Mumbai', '001')''')
    dbConnect.commit()
    dbConnect.close()

# Create API key file holder. Does not request or return any value.
# CREATE privVars.py file.
# Contains Default location, DarkSky and Google API key.
def createVarFile():
    print("Preparing key storage...")
    print("Note key storage is not encrypted (yet). Do not initialize on public PCs.")
    with open('tmpr.py', 'w') as var:
        print('darksky Weather API (Visit: https://darksky.net/dev/account) ')
        WtrKey = input('darksky API key:')
        print('Google Maps API key [UNUSED. CAN BE SKIPPED]')
        GooKey = input('Google Maps API key:')
        var.write('weatherApiKey = \'' +WtrKey +'\'' +'\n')
        var.write('GoogleAppKey = \'' +GooKey +'\'' +'\n')
        var.write('TestLoc = 18.9219841,72.8346543\n\n')
        var.write('''if __name__ == "__main__":
    print("This file contains all private variables. Please run from main.py instead.")''' +'\n')


# Main
# runs only when called self
# Creates database and variable/ API key holder file.
# TODO: Add argument support.
if __name__ == "__main__":
    # check for database
    print("Checking history database...")
    if not (os.path.isfile('hist.db')):
        # init history database
        createHistDB()
        print("database initialized for Location History!")
    else:
        # DB already exists. Skipping without checks...
        print('Database already exists. Skipping...')
    if not (os.path.isfile('tmpr.py')):
        createVarFile()
    else:
        print('variable file found. Skipping...')
else:
    print('press a to create database.\n press b to create variable file.\n press q to quit.')
    while(input() NOT q):
        if (input() = a):
            createHistDB()
            print("Database was created.")
        elif input() = b:
            createVarFile()
