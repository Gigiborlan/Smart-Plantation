# Smart-Plantation

## Project description

The Smart Plantation project aims to build an automated irrigation system for home gardens. Also, it collects and stores relevant data, such as moisture and temperature, so that it is possible to perform an analisys on the plants behavior in different environments.

The project has 3 major components:
* Arduino
* Raspberry pi
* Cloud Application

The Arduino is responsible for collecting data from the sensors and controlling the pump that irrigates the plant. The source code and some more information on the components can be found at https://github.com/Smart-Plantation/Arduino.

The Raspberry Pi is the bridge between the collected data and the could application. It also controlls time related functions, such as when the data is collected and stored, and the time of the day to irrigate the plant (which also depends on the soil moisture). Source code and further information: https://github.com/Smart-Plantation/Raspberry

And finally, the cloud application stores the collected data and displays it in a web page (Not completed yet).

## Application Description

This application stores the information received from the raspberry pi on a database. To run the application, the [Heroku plataform](https://www.heroku.com) was used. Also, the application database is Heroku Postgres (posgreSQL), which is included in the free resources.
