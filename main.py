import privVars as keys
import pycurl
import argparse
import io
import sqlite3

print (keys.weatherApiKey)

# Create Weather Database
def createWtrDB():
    dbConnect=sqlite3.connect('setup.db')
    cnt = dbConnect.cursor()
    cnt.execute('''CREATE TABLE wtr (geoTag text, FriendlyName text, lid number)''')
    cnt.commit()
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

createWtrDB()
