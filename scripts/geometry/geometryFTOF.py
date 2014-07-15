
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.detector.ftof   import FTOFDetectorFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D
import random
import math
from Particle import Particle


dataProvider = DataBaseLoader.getTimeOfFlightConstants()
print dataProvider.toString()

ftofDetector   = FTOFDetectorFactory.createDetector(dataProvider)
ftofDetector.show()

for slayer in range(0,3):
    ftofLayer = ftofDetector.getLayer(0,slayer,0)
    n = ftofLayer.numberOfComponents()
    for i in range(0,n):
        dr = ftofLayer.getDrawable(i,0.0)
        print ' path size = ',dr.nodes()
        print dr.toString()
        mid = ftofLayer.getMidpoint(i)
        len = ftofLayer.getLength(i)
        shape = ftofLayer.getShape(i)
        line  = ftofLayer.getLine(i)
        #print ' length = ',len, line.toString()
        nfaces = shape.size()
        #for face in range(0,nfaces):
        #    print shape.face(face).point(0).toString()
        #    print shape.face(face).point(1).toString()
        #    print shape.face(face).point(2).toString()

