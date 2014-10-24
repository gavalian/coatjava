#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.visualizer     import CLASVisualizer
from org.jlab.geom.detector.ec    import ECFactory
from org.jlab.geom.detector.ftof  import FTOFFactory
from org.jlab.geom.prim           import Transformation3D
from org.jlab.clas12.dbdata       import DataBaseLoader
from org.jlab.geom.prim           import Path3D,Face3D,Line3D,Point3D,Transformation3D
from java.lang import Math
from java.awt import Color
import random
import math
import sys

#===================================================================
# 
#===================================================================

data   = DataBaseLoader.getConstantsEC()
datasc = DataBaseLoader.getConstantsFTOF()
#print data.toString()

factory   = ECFactory()
factorysc = FTOFFactory()

ftofLayers = []
ecLayers   = []

for sector in range(0,6):
    eclayer = factory.createLayer(data,0,0,0)
    trans = Transformation3D()
    trans.translateXYZ(0.0,0.0,711.0)
    trans.rotateY(25.0/57.29)
    trans.rotateZ(sector*60.0/57.29)
    eclayer.setTransformation(trans)
    ecLayers.append(eclayer)
    transsc   = Transformation3D()
    transsc.translateXYZ(0.0,0.0,611.0)
    transsc.rotateY(25.0/57.29)
    transsc.rotateZ(sector*60.0/57.29)
    ftoflayer = factorysc.createLayer(datasc,0,0,0)
    ftoflayer.setTransformation(transsc)
    ftofLayers.append(ftoflayer)

#trans.show()
#ecDetector.setTransformation(trans)
#ecDetector = factory.createDetectorCLAS(data)

path = Path3D()
path.addPoint(0.0,0.0,0.0)
path.addPoint(200.0,0.0,900.0)

viewer = CLASVisualizer(100,100,1400,1200)
viewer.setBackgroundColor(Color(255,255,255))
viewer.getDisplay().setBackgroundColor(Color(255,255,255))
viewer.setVisible(True)
viewer.setTransparancy(0.5)

for layer in ecLayers:
    viewer.add(layer,Color(120,120,255))
for layer in ftofLayers:
    viewer.add(layer,Color(120,255,120))
#viewer.add(ecDetector,Color(120,120,255))
#viewer.add(path, Color(255,0,0))
viewer.update()
