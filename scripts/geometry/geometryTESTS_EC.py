
from org.jlab.detector.ec   import CLASECDetector
from org.jlab.detector.base import DetectorDescriptor

from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D
import random
import math
from Particle import Particle

ec = CLASECDetector()

for i in range(0,23):
    length   = ec.getLength(0,0,0,i)
    position = ec.getMidpoint(0,0,0,i)
    print 'Paddle details ',i
    print position.toString()
    print 'length = ',length,'\n\n'


for s in range(0,6):
    plane = ec.getPlane(s,0,0)
    print 'Sector = ',s+1
    print plane.point().toString(),
    print plane.normal().x(),plane.normal().y(),plane.normal().z(),'\n'
