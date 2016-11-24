import privVars as keys
import pycurl
import argparse
import io
import os
import sqlite3

print (keys.weatherApiKey)

# Create Weather Database
def createHistDB():
    dbConnect=sqlite3.connect('hist.db')
    cnt = dbConnect.cursor()
    cnt.execute('''CREATE TABLE wtr (geoTag text, FriendlyName text, lid number, wether object)''')
    dbConnect.commit()
    dbConnect.close()

# getWthr
# Accepts: location data
# Returns: Weather data (JSON)

def getWthr():
    #set storage and API link
    returnData = io.BytesIO()
    link = 'https://api.darksky.net/forecast/' + keys.weatherApiKey +'/19.211,72.874'

    # set instance
    connection = pycurl.Curl()

    #set options
    connection.setopt(connection.URL, link)
    connection.setopt(connection.WRITEFUNCTION, returnData.write)

    # perform cURL operation and close connection
    connection.perform()
    connection.close()

    return (returnData);

#print (getWthr())


#init history database
if not (os.path.isfile('setup.db')):
    createHistDB()
    print("database initialized for Location History!")
