# (c) 2016. Rohan Mishra
import privVars as keys
#import argparse
import os
#import sqlite3
#import googlemaps
import json
import requests

print("Powered by Dark Sky: https://darksky.net/poweredby/")
print ('Using API key: ' + keys.weatherApiKey)


# getWthr
# Accepts: location data
# Returns: Weather data (JSON)
def getWthr( loc ):
    #set storage and API link
    link = 'https://api.darksky.net/forecast/' + keys.weatherApiKey +'/' + loc
    print(link)

    # set instance
    req = requests.get(link)
    jsondata = json.loads(req.text)
    return jsondata

# getUserLoc
# Accepts: None
# returns: user location coordinates.
def getUserLoc():
    LocUrl = 'http://freegeoip.net/json'
    req = requests.get(LocUrl)
    j = json.loads(req.text)
    lat = j['latitude']
    lon = j['longitude']
    latlon = str(lat) + ',' + str(lon)
    return(latlon);

    # Setup Google Maps API
    #gmaps=googlemaps.Client(key=keys.GoogleAppKey)
    #getLocName = gmaps.reverse_geocode(latlon)
    #print(getLocName['formatted_address'])

# Main function.
# Calls getUserLoc() to get user location and getWthr() to get weather at that location.
# TODO: ADD support for arguments. Add history support.
if __name__ == "__main__":
    j = (getWthr(getUserLoc()))
    summary=j['currently'['summary']]
    temperature = j['currently'['temperature']]
    print('looks like its ' + summary + 'outside. Its ' +  temperature + 'Degrees.' )
