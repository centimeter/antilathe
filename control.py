import RPi.GPIO as GPIO
import time
 
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
      self.setStep(1, 0, 1, 0)
      time.sleep(delay)
      self.setStep(0, 1, 1, 0)
      time.sleep(delay)
      self.setStep(0, 1, 0, 1)
      time.sleep(delay)
      self.setStep(1, 0, 0, 1)
      time.sleep(delay)
   
  def backwards(self, delay, steps):  
    for i in range(0, steps):
      self.setStep(1, 0, 0, 1)
      time.sleep(delay)
      self.setStep(0, 1, 0, 1)
      time.sleep(delay)
      self.setStep(0, 1, 1, 0)
      time.sleep(delay)
      self.setStep(1, 0, 1, 0)
      time.sleep(delay)
   
    
  def setStep(self, w1, w2, w3, w4):
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

if __name__ == "__main__":
  x = Stepper(2,3,4,17)
  y = Stepper(27,22,10,9)
  theta = Stepper(11,0,5,6)
  extrude = Stepper(13,19,26,21)
  GPIO.cleanup()



