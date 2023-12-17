#!/usr/bin/python

import minimalmodbus
import serial
import time

MODBUSDEV='/dev/ttyUSB0' # usb device to connect to RS485 RTU Modbus
#MODBUSSLAVEADRESS=2  # default 1 according R4DCB08 datasheet
MODBUSSLAVEADRESS=3  # default 1 according R4DCB08 datasheet

instrument = minimalmodbus.Instrument(MODBUSDEV, MODBUSSLAVEADRESS,  minimalmodbus.MODE_RTU)  # port name, slave address (in decimal) according to R4DCB08 data sheet

instrument.debug = False
#instrument.debug = True
instrument.serial.timeout = 1.0
instrument.timeout = 1.0

instrument.baudrate = 9600
instrument.serial.baudrate = 9600
#instrument.close_port_after_each_call = True

print(instrument)

temps=[]
for i in range(8):
	temps.append(-3276.8)

print(temps)

## Read temperature (PV = ProcessValue) ##
#for x in range (0, 3):
for x in range (0, 8):
	try:
		print("try to read temp {}".format(x))
		temperature = instrument.read_register(x,1,3,True )  # Registernumber, number of decimals,functioncode=3,signed
		print("temperatur {} = {} C".format(x,temperature))
		temps[x]=temperature
		time.sleep(0.2)
	except Exception as e:
		print( "Error: %s" % str(e) )


print("read temperatures:")
print(temps)

## read baudrate 
print("read baudrate")
try:
        baudrate = instrument.read_register(255,1,3) # Hexa FF
        print("baudrate={} 0=1200,1=2400,2=4800 ,3=9600(funzt bei Dirk), 4=19200  ".format(baudrate*10))
except Exception as e:
        print( "Error: %s" % str(e) )

## read RS485adress
print("read RS485 adress")
try:
        rs485adress = instrument.read_register(254,1,3) # Hexa FE
        print("rs485adresse={} ".format(rs485adress*10))
except Exception as e:
        print( "Error: %s" % str(e) )



