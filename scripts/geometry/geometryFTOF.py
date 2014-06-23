
from org.jlab.detector.ftof import CLASFTOFDetector
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D
import random
import math
from Particle import Particle


ftof = CLASFTOFDetector()
ftof.initXML('../../lib/geometry/FTOFPaddles_CLAS.xml')

for i in range(0,23):
    length   = ftof.getLength(0,2,0,i)
    position = ftof.getMidpoint(0,2,0,i)
    print 'Paddle details ',i
    print position.toString()
    print 'length = ',length,'\n\n'


for s in range(0,6):
    plane = ftof.getPlane(s,0,0)

    print 'Sector = ',s+1
    print plane.point().toString(),
    print plane.normal().x(),plane.normal().y(),plane.normal().z(),'\n'
