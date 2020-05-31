import serial
import requests

temperature = None
moisture = None
watering = None

while(1):
	serial_reader = serial.Serial("/dev/ttyUSB0",9600)
	serial_reader.baudrate = 9600
	for i in range(0,3):
		serial_data = serial_reader.read(3)
		if serial_data[0] == 'T':
			temperature = serial_data[1] + serial_data[2]
			print("Temp: " + temperature)
		elif serial_data[0] == 'M':
			moisture = serial_data[1] + serial_data[2]
			print("Moist: " + moisture)
		elif serial_data[0] == 'W':
			watering = serial_data[2]
			print("Watering: " + watering)
		    
	r = requests.post('https://smart-plantation.herokuapp.com/data',params = {'temperature':temperature,'moisture':moisture,'watering':watering})
	print(r.status_code)




