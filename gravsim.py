import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

AU=(149.6e6 *1000)
scale=250/AU
G = 6.67428e-11

class body:
	def __init__(self,name,color,mass,px,py,vx,vy):
		self.name= name
		self.mass= mass
		self.px=px
		self.py=py
		self.vx=vx
		self.vy=vy
		self.positiony=[]
		self.positionx=[]
		self.color=color
	def gravity(self,other):
		sx,sy=self.px,self.py
		ox,oy =other.px,other.py
		dx=(ox-sx)
		dy=(oy-sy)
		distance=math.sqrt(dx**2+dy**2)
		if distance==0:
			raise ValueError('COLLISION')
		f=G*self.mass*other.mass/(distance**2)
		theta = math.atan2(dy,dx)
		fx=math.cos(theta)*f
		fy=math.sin(theta)*f
		return [fx,fy]
#plt.ion()

def simulate(bodies):
	timestep= 24*3600
	step = 1 

	#for body in bodies:
	#		plt.plot(body.px,body.py,body.color+'o')
	while step<=2000:
		print str(step)
		
		step+=1
		force= {}
		for body in bodies:
			total_fx=total_fy=0.0
			for other in bodies:
				if body is other:
					continue
				fx,fy=body.gravity(other)
				total_fx+=fx
				total_fy+=fy
			force[body]=(total_fx,total_fy)
		for body in bodies:
			fx,fy=force[body]
			body.vx +=fx/body.mass*timestep
			body.vy+=fy/body.mass*timestep
			body.px +=body.vx*timestep
			body.py+=body.vy*timestep
			body.positiony.append(body.py*scale)
			body.positionx.append(body.px*scale)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')		
	for body in bodies:
		ax.scatter(body.positionx,body.positiony, c=body.color,marker='o')
	#plt.close(fig)

def runstuff():
	sun = body('sun','y',1.98892*10**30,0,0,0,0)
	earth = body('earth','g',5.9742*10**24,-1*AU,0,0,29.783*1000)
	venus =body('venus','r',4.8685*10**24,0.723*AU,0,0,-35.02*1000)
	jupiter = body('jupiter','k', 1.898*10**27,4.2*AU,0,0,-13.1*1000)
	simulate([sun,earth,venus,jupiter])
runstuff()

