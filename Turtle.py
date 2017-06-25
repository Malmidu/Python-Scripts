import math
import turtle
import sys, random, argparse
import random
from fractions import gcd
# Draw the circle using turtle



class Spiro:
	#Contructor
	def __init__(self, xc, yc, col, R, r, l):
		
		#Create the turtle object
		self.t = turtle.Turtle()
		#set the cursor shape
		self.t.shape('turtle')
		#set the step in degrees
		self.step = 5
		#Set the drawing complete flag
		self.drawingComplete = False
		#Set the parameters
		self.setparams(xc, yc, col, R, r, l)
		#initialize the drawing
		self.restart()
		
	def setparams(self, xc, yc, col, R, r, l):
		self.xc = xc
		self.yc = yc
		self.R = int(R)
		self.r = int(r)
		self.l = l
		self.col = col
		#reduce r/R to its cmalled for by dividing with the GCD
		
		gcdVal = gcd(self.r, self.R)
		self.nRot = self.r//gcdVal
		#get ratio of radii
		self.k = r/float(R)
		#set the color
		self.t.color(*col)
		#store the current angle
		self.a = 0
	
	def restart(self):
		#set the flag
		self.drawingComplete = False
		#show the turtle
		self.t.showturtle()
		#go to the first point
		self.t.up()
		R, k, l = self.R, self.k, self.l
		a = 0.0
		x = R*((l-k)*math.cos(a) + l*k*math.cos((l-k)*a/k))
		y = R*((l-k)*math.sin(a) - l*k*math.sin((l-k)*a/k))
		self.t.setpos(self.xc + x, self.yc + y)
		self.t.down()
	
	def draw(self):
		#draw the rest of the points
		R, k, l = self.R, self.k, self.l
		for i in range(0, 360*self.nRot + 1, self.step):
			a = math.radians(i)
			x = R*((l-k)*math.cos(a) + l*k*math.cos((l-k)*a/k))
			y = R*((l-k)*math.sin(a) - l*k*math.sin((l-k)*a/k))
			
			self.t.setpos(self.xc + x, self.yc + y)
			
			#drawing is now done so hide the turtle cursor
			self.t.hideturtle()
	
	def update(self):
		#skip the rest of the steps if donw
		if self.drawingComplete:
			return
		#increment the angle
		self.a += self.step
		#draw a step
		R, k, l = self.R, self.k, self.l
		#set the angle
		a = math.radians(self.a)
		x = R*((l-k)*math.cos(a) + l*k*math.cos((l-k)*a/k))
		y = R*((l-k)*math.sin(a) - l*k*math.sin((l-k)*a/k))
		self.t.setpos(self.xc + x, self.yc + y)
		# if drawing is complete set the flag
		if self.a >= 360*self.nRot:
			self.drawingComplete = True
			self.t.hideturtle()
			
	def clear(self):
		self.t.clear()
			
class SpiroAnimator:
	# constructor
	def __init__(self, N):
		# set the timer value in milliseconds
		self.deltaT = 10
		#get the window dimensions
		self.width = turtle.window_width()
		self.height = turtle.window_height()
		#create the spiro object
		self.spiros = []
		for i in range(N):
			#Generate random parameters
			rparams = self.genRanomParams()
			#set the spiro parameters
			spiro = Spiro(*rparams)
			self.spiros.append(spiro)
			#call timer
		turtle.ontimer(self.update, self.deltaT)
	def genRanomParams(self):
		width, height = self.width, self.height
		R = random.randint(50, min(width, height)//2)
		r = random.randint(10, 9*R//10)
		l = random.uniform(0.1, 0.9)
		xc = random.randint(-width//2, width//2)
		yc = random.randint(-height//2, height//2)
		col = (random.random(), random.random(), random.random())
		
		return (xc, yc, col, R, r, l)
	
	def restart(self):
		for spiro in self.spiros:
			#clear
			spiro.clear()
			#generate random parameters
			rparams = self.genRanomParams()
			# set the spiro parameters
			spiro.setparams(*rparams)
			#restart drawing
			spiro.restart()
	
	def update(self):
		#update all spiros
		nComplete = 0
		for spiro in self.spiros:
			#update
			spiro.update()
			#count completed spiros
			if spiro.drawingComplete:
				nComplete += 1
		if nComplete == len(self.spiros):
			self.restart()
		#call the timer
		turtle.ontimer(self.update, self.deltaT)
		
	def toggleTurtles(self):
		for spiro in self.spiros:
			if spiro.t.isvisible():
				spiro.t.hideturtle()
			else:
				spiro.t.showturtle()
		
	

		
def drawCircleTurtle(x, y, r):
	#Move to the start of the circle
	
	turtle.up()
	turtle.setpos(x+r, y)
	turtle.down()
	
	#Draw the circle
	for i in range(0, 365, 5):
		a = math.radians(i)
		turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))
		
# drawCircleTurtle(100, 100, 50)
# turtle.mainloop()

def main():
	print("generating spirograph...")
	
	descStr = """ This program draws spirographs using the turtle module.
	When run with no arguments, this program draws random spirographs.
		Terminology
		
		R: radius of the outer circle
		r: radius of the inner circler
		l: ratio of hole distance to r
		"""
	parser = argparse.ArgumentParser(description=descStr)
	
	#add expected arguements
	parser.add_argument('--sparams', nargs=3, dest='sparams', required = False, help='The three arguments in sparams: R, r, l.')
	
	parser.add_argument('--t', type = int, dest='turtNum', required = False, help='Set the number of turtles to be created if no parameters are given')
	
	#parse args
	args = parser.parse_args()
	
	#set the width of the window to 80 percent of screen width
	turtle.setup(width=0.8)
	
	#set the cursor shape to turtle
	turtle.shape('turtle')
	
	#set the title to spirographs!
	turtle.title("Spirographs!")
	
	#add the key handler to save drawings OMMITTED THIS	
	#turtle.onkey(saveDrawing, "s")
	
	#start listening
	turtle.listen()
	
	#hide the main turtle cursor
	turtle.hideturtle()
	
	if args.sparams:
		params = [float(x) for x in args.sparams]
		#draw the spirograph with the given parameters
		
		col = (0.0, 0.0, 0.0)
		spiro = Spiro(0, 0, col, *params)
		spiro.draw()
	else:
		
		#create the animator object
		if args.turtNum:
			spiroAnim = SpiroAnimator(int(args.turtNum))
		else:
		
			spiroAnim = SpiroAnimator(4)
		#add a key handler to toggle the turtle cursor
		turtle.onkey(spiroAnim.toggleTurtles, "t")
		#add a key handler to restart the animation
		turtle.onkey(spiroAnim.restart, "space")
		turtle.onkey(exit, "x")
	#start the turtle mainloop
	turtle.mainloop()

if __name__ == "__main__":
		main()