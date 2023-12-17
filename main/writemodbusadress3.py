#!/usr/bin/python

import minimalmodbus
import serial
import time

#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1,  minimalmodbus.MODE_RTU)  # port name, slave address (in decimal)
# slaveaddress (int): Slave address in the range 1 to 247 (use decimal numbers, not hex). Address 0 is for broadcast, and 248-255 are reserved.
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1,  minimalmodbus.MODE_RTU)  # port name, slave address (in decimal)
#instrument.debug = False
instrument.debug = True
#instrument.TIMEOUT = 0.1
#instrument.serial.timeout = 0.1
#instrument.timeout = 0.1
#instrument.timeout = 0.1
instrument.serial.timeout = 1.0
instrument.timeout = 1.0

instrument.baudrate = 9600
instrument.serial.baudrate = 9600
#instrument.close_port_after_each_call = True

print(instrument)


print("!!!!!")
print("write RS485 adress to 3 - Warning only on board should be connected to modbus!")
try:
        reply = instrument.write_register(254,0.3,1,6,False) # registeraddress=254(Hexa FE), value=0.3(neueZielSlaveadresse 0.3 cause internally minimalmodbus multiplies by 10), number_of_decimals=1, functioncode=6 (schreibe),signed=False
        print("rs485adresse={} ".format(reply))
except Exception as e:
        print( "Error: %s" % str(e) )



