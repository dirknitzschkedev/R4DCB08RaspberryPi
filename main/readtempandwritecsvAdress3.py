#!/usr/bin/python

import minimalmodbus #sudo pip install minimalmodbus
import serial
import time
import pytz   #sudo pip install pytz
import csv
from datetime import datetime, date, time

# modify these values if needed
MODBUSDEV='/dev/ttyUSB0' # usb device to connect to RS485 RTU Modbus
MODBUSSLAVEADRESS=3  # default 1 according R4DCB08 datasheet
DATAFOLDER='/home/pi/modbus/data/csvfiles/'
CSVFILENAME='temperature_adress3.csv'
INFLUX_TIMESTAMPFORMAT="%Y-%m-%d_%H:%M:%S%z"
CSVFODERANDFILENAME=DATAFOLDER+CSVFILENAME
csvheaders = ['timestamp','R4DCB08_3_temp1','R4DCB08_3_temp2','R4DCB08_3_temp3','R4DCB08_3_temp4','R4DCB08_3_temp5','R4DCB08_3_temp6','R4DCB08_3_temp7','R4DCB08_3_temp8']


#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1,  minimalmodbus.MODE_RTU)  # port name, slave address (in decimal) according to R4DCB08 data sheet
instrument = minimalmodbus.Instrument(MODBUSDEV, MODBUSSLAVEADRESS,  minimalmodbus.MODE_RTU)  # port name, slave address (in decimal) according to R4DCB08 data sheet
instrument.debug = False
#instrument.debug = True
instrument.serial.timeout = 1.0
instrument.timeout = 1.0

instrument.baudrate = 9600
instrument.serial.baudrate = 9600

print(instrument)

now=datetime.now(pytz.timezone('Europe/Berlin'))
currenttimestamp=now.strftime(INFLUX_TIMESTAMPFORMAT)
# print(currenttimestamp)


temps=[]
temps.append(currenttimestamp)
for i in range(8):
	temps.append(-3276.8)

#print(temps) # disable comment for debug reasons

## Read temperature (PV = ProcessValue) ##
for x in range (0, 8):
	try:
		print("try to read temp {}".format(x))
		#temperature = instrument.read_register(x,1,3,False )  # Registernumber 0-8 shows temperatures of channel 1-8 according to R4DCB08 data sheet
		temperature = instrument.read_register(x,1,3,True )  # Registernumber, number of decimals,functioncode=3,signed
		print("temperatur {} = {} C".format(x,temperature))
		temps[x+1]=temperature
		#time.sleep(0.2)
	except Exception as e:
		print( "Error: %s" % str(e) )


print("read temperatures:")
print(temps)

## read baudrate 
print("read baudrate")
try:
        baudrate = instrument.read_register(255,1,3) # Hexa FF=255 shows RS485 RTU Modbus baud rate according to R4DCB08 data sheet 
        print("baudrate={} 0=1200,1=2400,2=4800 ,3=9600(works for me stable), 4=19200  ".format(baudrate*10))
except Exception as e:
        print( "Error: %s" % str(e) )

## read RS485adress
print("read RS485 adress")
try:
        rs485adress = instrument.read_register(254,1,3) # Hexa FE=254 shows RS485 RTU Modbus adress according to R4DCB08 data sheet 
        print("rs485adresse={} ".format(rs485adress*10)) 
except Exception as e:
        print( "Error: %s" % str(e) )


print("writing csv file {}".format(CSVFODERANDFILENAME))
with open(CSVFODERANDFILENAME, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(csvheaders)
    writer.writerow(temps)
csvfile.close()
