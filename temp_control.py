import serial, string, time
import RPi.GPIO as GPIO

output = " "
ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout = 1)

for i in range(0,256):
	print unichr(i)
	ser.write(chr(i))
	time.sleep(1) 

# if int(i) >= 230
# 	GPIO.output(1, GPIO.LOW)
# else 
# 	GPIO.output(1, GPIO.HIGH)
	