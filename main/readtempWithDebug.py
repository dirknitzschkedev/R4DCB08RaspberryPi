#!/usr/bin/python

import minimalmodbus
import serial

#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 3)  # port name, slave address (in decimal)
#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 3, 'rtu')  # port name, slave address (in decimal)
#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1, 'rtu')  # port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1,  minimalmodbus.MODE_RTU)  # port name, slave address (in decimal)
instrument.debug = True
# Dirk Timeout is not working
#instrument.TIMEOUT = 0.1
#instrument.serial.timeout = 0.1
#instrument.timeout(0.1)
instrument.debug = 0.1

instrument.baudrate = 9600
instrument.serial.baudrate = 9600

print(instrument)


## Read temperature (PV = ProcessValue) ##
for x in range (0, 3):
	try:
		#temperature = instrument.read_register(x, 1, 3, True)  # Registernumber, number of decimals
		#temperature = instrument.read_register(x, 0, 3, True)  # Registernumber, number of decimals
		#temperature = instrument.read_register(x )  # Registernumber, number of decimals
		temperature = instrument.read_register(x,1,3,False )  # Registernumber, number of decimals
		print("temperature register {} =".format(x))
		print(temperature)
		print("temperatur {} = {}".format(x,temperature))
	except Exception as e:
		print( "Error: %s" % str(e) )
