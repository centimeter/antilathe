from control import Stepper
from pygame import key

if __name__ == "__main__":
  x = Stepper(2,3,4,17)
  y = Stepper(27,22,10,9)
  theta = Stepper(11,0,5,6)
  extrude = Stepper(13,19,26,21)
  delay = 10

  if True:

  	keys = pygame.get_pressed() 
  	if keys[pygame.K_UP]:
  		y.forward(delay, 1)
  	if keys[pygame.K_DOWN]:
  		y.reverse(delay, 1)
  	if keys[pygame.K_RIGHT]:
  		x.forward(delay, 1)
  	if keys[pygame.K_LEFT]:
  		x.reverse(delay, 1)
  	if keys[pygame.k_E]:
  		extrude.forward(delay,1)
  	if keys[pygame.k_R]:
  		extrude.reverse(delay,1)