from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from org.jlab.geom.detector.ec   import ECFactory
from org.jlab.clas12.dbdata import DataBaseLoader
import random
import math


rootVolume  = Point3D(2170.0799,0.0,6789.8397)
layerVolume = Point3D(0.0,0.0,-9.03)
paddle      = Point3D(-0.668675418863381,0,0)

data = DataBaseLoader.getCalorimeterConstants()
factory = ECFactory()
ecDetector   = factory.createDetectorCLAS(data)

line = ecDetector.getSector(0).getSuperlayer(0).getLayer(0).getComponent(42).getLine()
print line.midpoint().toString()
mid = line.midpoint()

print 'paddle = ', paddle.toString()
#paddle.translateXYZ(0.,0.,-90.3)
#paddle.translateXYZ(rootVolume.x(),rootVolume.y(),rootVolume.z())
print 'paddle translated = ', paddle.toString()
rV = Point3D(mid.x()-paddle.x(),mid.y()-paddle.y(),mid.z()-paddle.z()+9.03)
print 'coord = ', rV.toString()
paddle.translateXYZ(0.,0.,-9.3)
paddle.translateXYZ(rV.x(),rV.y(),rV.z())
print 'paddle translated = ', paddle.toString()
