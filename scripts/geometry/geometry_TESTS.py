
from org.jlab.detector.ftof import CLASFTOFDetector
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D
import random
import math
from Particle import Particle


ftof = CLASFTOFDetector()
ftof.initXML('../../lib/geometry/FTOFPaddles_CLAS.xml')

sector = 0

for c in range(0,23):
    desc = DetectorDescriptor(0,sector,0,0,c)
    print desc.isValid()
    print ftof.getMidpoint(desc).x(),ftof.getMidpoint(desc).y(),ftof.getMidpoint(desc).z(),ftof.getLength(desc)
    line = ftof.getLine(0,0,0,c)
    print 'LINE',line.origin().x(),line.origin().y(),line.origin().z()
    print 'LINE',line.end().x(),line.end().y(),line.end().z()
    desc.set(0,0,0,0,0)
    plane = ftof.getPlane(desc)
    print plane.toString()

alpha = 30.0/57.29
x2 = 700.0*math.cos(alpha)
y2 = 700.0*math.sin(alpha)
x3 = 700.0*math.cos(-alpha)
y3 = 700.0*math.sin(-alpha)
face_s1 = Face3D(0.0,0.0,600.0,x2,y2,600.0,x3,y3,600.0)

p = Particle()
point = Point3D()
for i in range(0,100):
    print '>>>>>>>>>>>>>>>>>> EVENT = ',i
    p.setRandom(11,-1)
    path = p.getPath()
    print path.toString()
    line = Line3D(path.getNode(0),path.getNode(1))
    if Face3D.intersection(face_s1,line,point)==True:
        print 'found intersection---> ', point.x(),point.y(),point.z()
    else:
        print '--------->  no intersection'
    hits = ftof.getLayerHits(path)
    if hits.size()>0:
        print '-------------> hit list.............. size = ',hits.size()
    #print path.toString()
