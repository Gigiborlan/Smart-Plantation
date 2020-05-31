print(__name__)
from app import app
from flask import Response, request

_temperature = 0
_umidity = 0
_watering = 0

@app.route('/')
@app.route('/status')
def status():
    return Response("up",200)

@app.route('/data',methods=['GET'])
def read_temperature():
    global _temperature, _umidity
    return "Temperatura: " + str(_temperature) + "oC\nUmidade: " + str(_umidity) + "%\nWatering" + str(_watering)

@app.route('/data',methods=['POST'])
def set_data():
    global _temperature, _umidity
    temperature = request.args.get('temperature')
    if temperature is not None:
		_temperature = temperature
    umidity = request.args.get('umidity')
    if umidity is not None:
		_umidity = umidity
    watering = request.args.get('watering')
    if watering is not None:
		_watering = watering
    return Response("Posted",200)
