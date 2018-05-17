from control import Stepper
import pygame
import atexit 
pygame.init()
pygame.display.set_mode()
if __name__ == "__main__":
  x = Stepper(2,3,4,17)
  y = Stepper(27,22,10,9)
  theta = Stepper(11,0,5,6)
  extrude = Stepper(13,19,26,21)
  delay = 10

  while True:

  	keys = pygame.key.get_pressed() 
  	if keys[pygame.K_UP]:
  		y.forward(delay, 1)
  		print("forward")
  	if keys[pygame.K_DOWN]:
  		y.reverse(delay, 1)
  	if keys[pygame.K_RIGHT]:
  		x.forward(delay, 1)
  	if keys[pygame.K_LEFT]:
  		x.reverse(delay, 1)
  	if keys[pygame.K_e]:
  		extrude.forward(delay,1)
  	if keys[pygame.K_r]:
  		extrude.reverse(delay,1)

def exit_handler():
  GPIO.cleanup()
