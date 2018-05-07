from control import Stepper

if __name__ == "__main__":
  x = Stepper(2,3,4,17)
  y = Stepper(27,22,10,9)
  theta = Stepper(11,0,5,6)
  extrude = Stepper(13,19,26,21)
  delay = 10
  x_dir = False
  #moves out a layer every time
  for shell in range(10):
  	x_dir=!x_dir
  	#move to the right vaguely
  	for pos in range(100):
  		#spin the spindle
  		for spin in range(10):
  			#extrude the extruder
  			theta.forward(delay,1)
  			extrude.forward(delay,1)
  		if x_dir:
  			x.forward(delay, 1)
  		else:
  			x.reverse(delay, 1)
  	y.forward(delay, 1)