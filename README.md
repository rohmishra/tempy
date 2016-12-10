# Tempy Weather

###### A simple FOSS Weather App.

Tempy weather is a open source weather app designed to be usefull while being minimal.

##  IMPORTANT!

Tempy needs to be setup first in order to be run. This is a one time requirment and can be done by navingating to the Tempy's folder and running the 'setup.py' file.

> user@system ~/Projects/Tempy > python3 setup.py

Please refer to [Getting Started](#getting-started) Section for detailed information.

## Getting Started

### Downloading Tempy

The Tempy project is available on and can be downloaded from github here: https://github.com/rohmishra/tempy

You can also use git to clone the repository to your desktop. Please note that you need to have git installed on your system to be able to perform this action.

Navigate to folder where you want to clone the git repository and run the following command in terminal:

> git clone https://github.com/rohmishra/tempy.git

## Setting up Tempy

As of now, you dont need to install Tempy in order to use it. However, you need to set it up by providing appropriate API keys for it to function.

You need application keys for following services:

*   Your preffered weather provider. (currently only Dark Sky is supported.)
*   Google Services

To setup Tempy, make sure you are in the directory where you have cloned Tempy.

![](docs/img/term-ls.png?nocache2650=1481364119163)  

Run the setup.py script to setup Tempy:

> user@system ~/Projects/Tempy > pthon3 setup.py

## Using Tempy

Currently Tempy only allows you to view basic weather information about current location (determined by your IP adderess). Support for custom loactions and detailed information is coming soon-ish!

To run Tempy:

> user@system ~/Projects/Tempy > pthon3 main.py

## Sources

Currently, Tempy uses following sources for weather retrival

*   Dark Sky
*   <strike>OpenWeatherMap API</strike>

Tempy Also uses the following services for geolocation and other location mapping services

*   freegeoip.net
*   <strike>Google Maps API</strike>

## Privacy

No data gathered by Tempy is sent to its original creator. The data may be temperorarily stored locally on your machine in form of cached data or in SQLite database mainatined by Tempy. Please refer to service providers' (listed in sources) privacy policy for futher details. Tempy's developer does not control and is not responsible for management of data by third party soures.