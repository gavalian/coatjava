import math
import random
from org.jlab.vector import Vector3D
from org.jlab.geom   import Point3D
from org.jlab.geom   import Path3D

class Particle:
    def __init__(self):
        self.origin = Point3D(0.0,0.0,0.0)
        self.vector = Vector3D(0.0,0.0,0.0)
        self.pid    = 11
        self.charge = -1
        self.theta_min = 10.0
        self.theta_max = 45.0
        self.mom_min   = 1.0
        self.mom_max   = 6.0

    def setPid(self,id,c):
        self.pid = id
        self.charge = c

    def setOrigin(self,x,y,z):
        self.origin.set(x,y,z)
    
    def setVector(self,px,py,pz):
        self.vector.setXYZ(px,py,pz)

    def getPath(self):
        path = Path3D()
        path.generate(self.origin.x(),self.origin.y(),self.origin.z(),self.vector.x(),self.vector.y(),self.vector.z(),2000.0,3)
        #path.addPoint(0.,0.,0.)
        #x = 1000.0*math.sin(self.vector.theta())*math.cos(self.vector.phi())
        #y = 1000.0*math.sin(self.vector.theta())*math.sin(self.vector.phi())
        #z = 1000.0*math.cos(self.vector.theta())
        #path.addPoint(x,y,z)
        return path

    def setRandom(self,id,c):
        self.pid    = id
        self.charge = c
        theta = (random.random()*(self.theta_max-self.theta_min)+self.theta_min)/57.29
        phi   = (random.random()*360.0-180.0)/57.29
        mom   = random.random()*(self.mom_max-self.mom_min) + self.mom_min
        self.vector.setXYZ(mom*math.sin(theta)*math.cos(phi),mom*math.sin(theta)*math.sin(phi),mom*math.cos(theta))
    def printInfo(self):
        print 'PARTICLE : ',
        print 'origin ( ',self.origin.x(),self.origin.y(),self.origin.z(),' )  ',
        print 'vector ( ',self.vector.x(),self.vector.y(),self.vector.z(),' )'
