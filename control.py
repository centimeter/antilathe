import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 

class Stepper():

  def __init__(self, a1, a2, b1, b2):
    self.a1 = a1
    self.a2 = a2
    self.b1 = b1
    self.b2 = b2
     
    GPIO.setup(coil_A_1_pin, GPIO.OUT)
    GPIO.setup(coil_A_2_pin, GPIO.OUT)
    GPIO.setup(coil_B_1_pin, GPIO.OUT)
    GPIO.setup(coil_B_2_pin, GPIO.OUT)
     
  def forward(delay, steps):  
    for i in range(0, steps):
      setStep(1, 0, 1, 0)
      time.sleep(delay)
      setStep(0, 1, 1, 0)
      time.sleep(delay)
      setStep(0, 1, 0, 1)
      time.sleep(delay)
      setStep(1, 0, 0, 1)
      time.sleep(delay)
   
  def backwards(delay, steps):  
    for i in range(0, steps):
      setStep(1, 0, 0, 1)
      time.sleep(delay)
      setStep(0, 1, 0, 1)
      time.sleep(delay)
      setStep(0, 1, 1, 0)
      time.sleep(delay)
      setStep(1, 0, 1, 0)
      time.sleep(delay)
   
    
  def setStep(w1, w2, w3, w4):
    GPIO.output(self.a1, w1)
    GPIO.output(self.a2, w2) 
    GPIO.output(self.b1, w3)
    GPIO.output(self.b2, w4)
 
class Printer():
  def __init__(self):
    x = Stepper(2,3,4,17)
    y = Stepper(27,22,10,9)
    theta = Stepper(11,0,5,6)
    extrude = Stepper(13,19,26,21)
    delay = 10
    x_dir = False

while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forward(int(delay) / 1000.0, int(steps))
  steps = raw_input("How many steps backwards? ")
  backwards(int(delay) / 1000.0, int(steps))

if __name__ == "__main__":
  x = Stepper(2,3,4,17)
  y = Stepper(27,22,10,9)
  theta = Stepper(11,0,5,6)
  extrude = Stepper(13,19,26,21)