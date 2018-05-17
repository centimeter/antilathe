import RPi.GPIO as GPIO
import time
import serial
 
GPIO.setmode(GPIO.BCM)
 

class Stepper():

  def __init__(self, a1, a2, b1, b2):
    self.a1 = a1
    self.a2 = a2
    self.b1 = b1
    self.b2 = b2
    
    GPIO.setup(self.a1, GPIO.OUT)
    GPIO.setup(self.a2, GPIO.OUT)
    GPIO.setup(self.b1, GPIO.OUT)
    GPIO.setup(self.b2, GPIO.OUT)
     
  def forward(self, delay, steps):  
    for i in range(0, steps):
      self.self.setStep(1, 0, 1, 0)
      time.sleep(delay)
      self.self.setStep(0, 1, 1, 0)
      time.sleep(delay)
      self.self.setStep(0, 1, 0, 1)
      time.sleep(delay)
      self.self.setStep(1, 0, 0, 1)
      time.sleep(delay)
   
  def backwards(self, delay, steps):  
    for i in range(0, steps):
      self.self.setStep(1, 0, 0, 1)
      time.sleep(delay)
      self.self.setStep(0, 1, 0, 1)
      time.sleep(delay)
      self.self.setStep(0, 1, 1, 0)
      time.sleep(delay)
      self.self.setStep(1, 0, 1, 0)
      time.sleep(delay)
   
    
  def self.setStep(self, w1, w2, w3, w4):
    GPIO.output(self.a1, w1)
    GPIO.output(self.a2, w2) 
    GPIO.output(self.b1, w3)
    GPIO.output(self.b2, w4)
 
class BiDiStepper():
  def __init__(self, pwma, pwmb, dira, dirb):
    self.pwm_a = pwma
    self.pwm_b = pwmb
    self.dir_a = dira
    self.dir_b = dirb

    GPIO.setup(self.pwm_a, GPIO.OUT)
    GPIO.setup(self.pwm_b, GPIO.OUT)
    GPIO.setup(self.dir_a, GPIO.OUT)
    GPIO.setup(self.dir_b, GPIO.OUT)

  def forward(self,delay, num_steps):
    for x in range(num_steps):
        self.setStep(1,0,1,0)
        time.sleep(delay)
        self.setStep(0,1,0,1)
        time.sleep(delay)
        self.setStep(1,0,0,0)
        time.sleep(delay)
        self.setStep(0,1,0,0)
        time.sleep(delay)
    self.setStep(0,0,0,0)

  def backward(self, delay, num_steps):
      for x in range(num_steps):
          self.setStep(0,1,0,0)
          time.sleep(delay)
          self.setStep(1,0,0,0)
          time.sleep(delay)
          self.setStep(0,1,0,1)
          time.sleep(delay)
          self.setStep(1,0,1,0)
          time.sleep(delay)
      self.setStep(0,0,0,0)
      
  def setStep(self, w1, w2, w3, w4):
    GPIO.output(pwm_a, w1)
    GPIO.output(pwm_b, w2)
    GPIO.output(dir_a, w3)
    GPIO.output(dir_b, w4)

class heater():
  def __init__(self, temp_pin):
    self.temp_pin - temp_pin 
    GPIO.setup(temp_pin, 1)
    self.ser = serial.Serial('/dev/ttyACM0',9600)

  def turnOn(self):
    GPIO.output(self.temp_pin, 1)
    print("On")

  def turnOff(self):
      GPIO.output(self.temp_pin, 0)
      print("Off")

  def adjust_temp(self, calib_min_T, calib_max_T):
   #this function will run forever, start it in a thread
    try:
      while True:
        raw_T = self.ser.readline()
        print(raw_T)
        raw_T = int(raw_T)
        if raw_T < calib_max_T:
            self.turnOff()
        elif raw_T > calib_min_T:
            self.turnOn()
        else:
            pass
    except KeyboardInterrupt():
      self.turnOff()
      print("power off")
    except:
      self.turnOff()
      print("power off")
    finally:
      ser.close()

class Printer():
  def __init__(self):
    x = Stepper(2,3,4,17)
    y = Stepper(27,22,10,9)
    theta = Stepper(11,0,5,6)
    extrude = Stepper(13,19,26,21)
    delay = 10
    x_dir = False





