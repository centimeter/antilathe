import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pwm_a = 17
pwm_b = 4
dir_a = 27
dir_b = 22

GPIO.setup(pwm_a, GPIO.OUT)
GPIO.setup(pwm_b, GPIO.OUT)
GPIO.setup(dir_a, GPIO.OUT)
GPIO.setup(dir_b, GPIO.OUT)

def forward(delay, num_steps):
    for x in range(num_steps):
        setStep(1,0,1,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,0,0)
        time.sleep(delay)
        setStep(0,1,0,0)
        time.sleep(delay)

def backward(delay, num_steps):
    for x in range(num_steps):
        setStep(0,1,0,0)
        time.sleep(delay)
        setStep(1,0,0,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,1,0)
        time.sleep(delay)
    
def setStep(w1, w2, w3, w4):
  GPIO.output(pwm_a, w1)
  GPIO.output(pwm_b, w2)
  GPIO.output(dir_a, w3)
  GPIO.output(dir_b, w4)

while True:
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forward(int(delay) / 1000.0, int(steps))
#  steps = raw_input("How many steps backwards? ")
#  backwards(int(delay) / 1000.0, int(steps))

