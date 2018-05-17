#!/usr/bin/python
import serial
import RPi.GPIO as GPIO

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
	while True:
		print ser.read(1000)
except KeyboardInterrupt:
	print "exiting..."
finally:
        ser.close()
        exit
