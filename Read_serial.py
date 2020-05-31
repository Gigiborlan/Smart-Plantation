import serial
import requests

while(1):
	serial_reader = serial.Serial("/dev/ttyUSB0",9600)
	serial_reader.baudrate = 9600
	serial_data = serial_reader.read(3)
	if serial_data[0] = 'T':
		temperature = serial_data[1] + serial_data[2]
	elif serial_data[0] = 'M':
		moisture = serial_data[1] + serial_data[2]
#	elif serial_data[0] = 'R':
	
#   requests.post('http://192.168.0.115:5000/data',params = {'temperature':temperature})

