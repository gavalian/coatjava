#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.ec   import ECFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from java.lang import Math
import random
import math
import sys

#===================================================================
# 
#===================================================================

thetaAngle = sys.argv[1]
phiAngle   = sys.argv[2]

data = DataBaseLoader.getCalorimeterConstants()
print data.toString()

factory = ECFactory()
ecDetector   = factory.createDetectorCLAS(data)
ecDetector.show()

pathMag   = 15000.0
pathPhi   = float(phiAngle)/57.29
pathTheta = float(thetaAngle)/57.29 

path = Path3D()
path.addPoint(0.0,0.0,0.0)
path.addPoint(pathMag*Math.sin(pathTheta)*Math.cos(pathPhi),pathMag*Math.sin(pathTheta)*Math.sin(pathPhi),pathMag*Math.cos(pathTheta))

hits = ecDetector.getHits(path)
print '\n-->\n'
for hit in hits:
    if(hit.getLayerId()<3):
        print hit.toString()


point = Point3D(0.0,0.0,697.7)
point.rotateY(25.0/59.27)

print point.toString()


#layer = ecDetector.getSector(0).getSuperlayer(0).getLayer(0)
layer   = factory.createLayer(data,0,0,0)
layerIN = factory.createLayer(data,0,0,1)

ncomp = layer.getNumComponents()

for i in range(0,ncomp):
    point = layer.getComponent(i).getMidpoint()
    #print 'PCAL U View Paddle ',i+1,point.toString()

layerIN = ecDetector.getSector(0).getSuperlayer(1).getLayer(0)

for i in range(0,layerIN.getNumComponents()):
    point = layerIN.getComponent(i).getMidpoint()
    #print 'ECINNER U View Paddle ',i+1,point.toString()
