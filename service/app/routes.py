print(__name__)
from app import app
from flask import Response, request

temperature = 0
umidity = 0

@app.route('/')
@app.route('/status')
def status():
    return Response("up",200)

@app.route('/data',methods=['GET'])
def read_temperature():
    global temperature, umidity
    return "Temperatura: " + str(temperature) + "oC"

@app.route('/data',methods=['POST'])
def set_data():
    global temperature, umidity
    temperature = request.args.get('temperature')
    print(temperature)
    umidity = request.args.get('umidity')
    return Response("Posted",200)