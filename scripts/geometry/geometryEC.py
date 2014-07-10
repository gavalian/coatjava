#================================================================
#================================================================
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D
from org.jlab.detector.ec   import ECDetectorFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom import Transformation3D
import random
import math
#================================================================
# 
#

provider = DataBaseLoader.getCalorimeterConstants()
print provider.toString()

ecLayerU  = ECDetectorFactory.INSTANCE.getLayer(provider,0,0,0)
ecLayerV  = ECDetectorFactory.INSTANCE.getLayer(provider,0,0,1)
ecLayerW  = ECDetectorFactory.INSTANCE.getLayer(provider,0,0,2)

tr = Transformation3D().rotateZ(-90./57.29).translateXYZ(0.,0.,620.0).rotateY(25./57.29).rotateZ(60./57.29)

#ecLayerU.setTransformation(tr)
#ecLayerV.setTransformation(tr)
#ecLayerW.setTransformation(tr)

ecLayerU.show()
ecLayerV.show()
ecLayerW.show()

surface = ecLayerV.getBoundary()

for i in range(0,surface.size()):
    print 'TLine *l = new TLine(',
    print surface.face(i).point(0).x(),',',
    print surface.face(i).point(0).y(),',',
    print surface.face(i).point(1).x(),',',
    print surface.face(i).point(1).y(),
    #print surface.face(i).point(0).z(),
    print ');\nl->Draw();'
    print 'TLine *l = new TLine(',
    print surface.face(i).point(1).x(),',',
    print surface.face(i).point(1).y(),',',
    print surface.face(i).point(2).x(),',',
    print surface.face(i).point(2).y(),
    print ');\nl->Draw();'
    print 'TLine *l = new TLine(',
    print surface.face(i).point(2).x(),',',
    print surface.face(i).point(2).y(),',',
    print surface.face(i).point(0).x(),',',
    print surface.face(i).point(0).y(),
    print ');\nl->Draw();'


print '-------------------------> EC Geometry \n\n'
ecGeom = ECDetectorFactory.INSTANCE.getDetector(provider)
ecGeom.show()

path = Path3D()

for i in range(0,2):
    path.generateRandom(0.,0.,0.,5.,55.,-180.,180.,15000,5)
    hits = ecGeom.getLayerHits(path)
    #print hits.size()
    for hit in hits:
        print hit.toString()
        #print hit.position().x(),hit.position().y(),hit.position().z()
