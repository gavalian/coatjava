#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.detector.ec   import ECDetectorFactory, ECLayerFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D,Transformation3D
import random
import math
from Particle import Particle

#===================================================================
# 
#===================================================================

dataProvider = DataBaseLoader.getCalorimeterConstants()
print dataProvider.toString()

ecDetector   = ECDetectorFactory.createDetector(dataProvider)
ecDetector.show()

print '\n\n\n------>'

ecLayerU     = ECLayerFactory.createLayer(dataProvider,0,0,0)
ecLayerU.show()
ecLayerV     = ECLayerFactory.createLayer(dataProvider,0,0,1)
ecLayerV.show()
ecLayerW     = ECLayerFactory.createLayer(dataProvider,0,0,2)
ecLayerW.show()


path = Path3D()

for i in range(0,10000):
    path.generateRandom(0.0,0.0,0.0,10.0,35.0,-180.,180.,15000.0,6)
    hits = ecDetector.getLayerHits(path)
    #print '-------------------------> EVENT ',i
    for hit in hits:
        #print hit.toString()
        print hit.getDescriptor().getLayer(),hit.getDescriptor().getComponent(),hit.position().x(),hit.position().y(),hit.position().z()


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