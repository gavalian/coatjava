#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.detector.dch  import DCDetectorFactory, DCLayerFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D,Transformation3D
import random
import math
from Particle import Particle

#===================================================================
# 
#===================================================================

dataProvider = DataBaseLoader.getDriftChamberConstants()
#print dataProvider.toString()

dcDetector   = DCDetectorFactory.createDetector(dataProvider)
#dcDetector.getLayer(0,0,0).show()
#dcDetector.show()

print '\n\n\n------>'

for s in range(0,6):
    print 'super Layer = ',s
    for i in range(0,6):
        dcLayerU     = dcDetector.getLayer(0,s,i)
        n = dcLayerU.numberOfComponents()
        print 'number of wires = ', n
        for w in range(0,n):
            wire = dcLayerU.getLine(w)
            print ' wire ----> ', w, wire.origin().x(),wire.origin().y(),wire.origin().z(),
            print wire.end().x(),wire.end().y(),wire.end().z()


#ecLayerV     = ECLayerFactory.createLayer(dataProvider,0,0,1)
#ecLayerV.show()
#ecLayerW     = ECLayerFactory.createLayer(dataProvider,0,0,2)
#ecLayerW.show()

#dcLayerU     = DCLayerFactory.createLayer(dataProvider,0,0,0)
#for i in range(0,112):
#    line = dcLayerU.getLine(i)
#print i,line.origin().x(),line.origin().y(),line.end().x(),line.end().y()

path = Path3D()

for i in range(0,1):
    path.generateRandom(0.0,0.0,0.0,10.0,35.0,-180.,180.,15000.0,6)
    hits = dcDetector.getLayerHits(path)
    #print '-------------------------> EVENT ',i, hits.size()
    for hit in hits:
        #print hit.toString()
        print hit.getDescriptor().getSector(),hit.getDescriptor().getSuperLayer(),hit.getDescriptor().getLayer(),hit.getDescriptor().getComponent(),
        print hit.position().x(),hit.position().y(),hit.position().z()


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
