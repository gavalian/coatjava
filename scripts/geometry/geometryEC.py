#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.ec   import ECFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
import random
import math

#===================================================================
# 
#===================================================================

data = DataBaseLoader.getCalorimeterConstants()
print data.toString()

factory = ECFactory()
ecDetector   = factory.createDetectorCLAS(data)
ecDetector.show()

path = Path3D()

for i in range(0,10000):
    path.generateRandom(0.0,0.0,0.0,5.0,10.0,-180.,180.,15000.0,6)
    #hits = ecDetector.getLayerHits(path)
    hits = ecDetector.getHits(path)
    print '-------------------------> EVENT ',i
    for hit in hits:
        print hit.toString()
#        print hit.getSector(),hit.position().x(),hit.position().y(),hit.position().z()


#surf = ecLayerV.getBoundary()
#for i in range(0,surf.size()):
#    face = surf.face(i)
#    print 'TLine *l = new TLine(',
#    print face.point(0).x(),',',
#    print face.point(0).y(),',',
#    print face.point(1).x(),',',
#    print face.point(1).y(),');'
#    print '\nl->Draw();\n'   
#    print 'TLine *l = new TLine(',
#    print face.point(1).x(),',',
#    print face.point(1).y(),',',
#    print face.point(2).x(),',',
#    print face.point(2).y(),');'
#    print '\nl->Draw();\n'
#    print 'TLine *l = new TLine(',
#    print face.point(2).x(),',',
#    print face.point(2).y(),',',
#    print face.point(0).x(),',',
#    print face.point(0).y(),');'
#    print '\nl->Draw();\n'
