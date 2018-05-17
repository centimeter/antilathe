import serial
import RPi.GPIO as GPIO

#Control the temnperature of an ATC Semit104GT-2 with a 4700KOhm pullup using a MOSFE

####Future implementation###########
#Operating temp ~200, do not go above 230
##max_T = 225 #Celsius
##min_T = 205
##
##calib_dict = {17:300,20:290,23:280,27:270,31:260,37:250,43:240,51:230,61:220,73:210,87:200,106:190,
##              128:180,155:170,189:160,230:150,278:140,336:130,402:120,476:110,554:100,635:90,713:80,
##              784:70,846:60,897:50,937:40,966:30,986:20,1000:10,1010:0}
##
##calib_max_T = 1000 #So that it starts with heater off
##calib_min_T = 0
##
##high = 1000
##low = 0

GPIO.setmode(GPIO.BCM)

temp_pin = 12
GPIO.setup(temp_pin, GPIO.OUT)

def turnOn():
    GPIO.output(temp_pin, 1)
    print("On")

def turnOff():
    GPIO.output(temp_pin, 0)
    print("Off")
#somewhere between 60 and 50
calib_min_T = 897   #about 83 for 205C
calib_max_T = 846  #about 56 for 225C

ser = serial.Serial('/dev/ttyACM0',9600)

try:
    while True:
        raw_T = ser.readline()
        print(raw_T)
        raw_T = int(raw_T)
        if raw_T < calib_max_T:
            turnOff()
        elif raw_T > calib_min_T:
            turnOn()
        else:
            pass

except KeyboardInterrupt():
    turnOff()
    print("Don't forget to power off!")

except:
    turnOff()
    print("Something is wrong! Power off!")

finally:
    ser.close()
    exit
