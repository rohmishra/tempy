import privVars as keys
import pycurl

print (keys.weatherApiKey)

#set storage and API link
returnData = None
link = 'https://api.darksky.net/forecast/' + keys.weatherApiKey +'/19.211,72.874'

# set instance
connection = pycurl.Curl()

#set options
connection.setopt(connection.URL, link)
connection.setopt(connection.WRITEDATA, returnData)

# perform cURL operation and close connection
connection.perform()
connection.close()

print (returnData)
