print(__name__)
from app import app
from flask import Response, request
#from app import database

_temperature = 0 # None, str
_moisture = 0
_watering = False

@app.route('/')
@app.route('/status')
def status():
    return Response("up",200)

@app.route('/data',methods=['GET'])
def read_temperature():
    global _temperature, _umidity, _watering
    # return 'Temperatura: {}oC\nUmidade: {}%\nWatering: {}'.format(str(_temperature), str(_moisture), str(_watering))
    return "Temperatura: " + str(_temperature) + "oC\nUmidade: " + str(_moisture) + "%\nWatering" + str(_watering)

@app.route('/data',methods=['POST'])
def set_data():
	global _temperature, _moisture, _watering
	temperature = request.args.get('temperature')
	if temperature is not None:
		_temperature = temperature
	moisture = request.args.get('moisture')
	print(moisture)
	if moisture is not None:
		_moisture = moisture
	watering = request.args.get('watering')
	if watering is not None:
		_watering = (watering == 1)
##		if watering == 1:
##			_watering = True
##		else:
##			_watering = False
	#database.insert_sensor_data(_temperature,_moisture,_watering)
	return Response("Posted",200)
