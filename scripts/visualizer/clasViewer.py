#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.visualizer    import CLASVisualizer
from org.jlab.geom.detector.bst  import BSTFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from java.lang import Math
from java.awt import Color
import random
import math
import sys

#===================================================================
# 
#===================================================================

data = DataBaseLoader.getConstantsBST()
print data.toString()

factory = BSTFactory()


viewer = CLASVisualizer(100,100,1400,1200)
viewer.setBackgroundColor(Color(150,150,255))
viewer.getDisplay().setBackgroundColor(Color(150,150,255))
viewer.setVisible(True)
viewer.setTransparancy(0.5)

path = Path3D()
path.addPoint(0.0,0.0,0.0)
path.addPoint(300.0,400.0,200.0)

#viewer.add(path,Color.WHITE)
for i in range(0,1):
    layer   = factory.createRingLayer(data,0,0,i)
    viewer.add(layer,Color(10,50,100))
    layer   = factory.createRingLayer(data,0,1,i)
    viewer.add(layer,Color(25,125,250))

#for i in range(0,10):
#    layer   = factory.createRingLayer(data,1,0,i)
#    viewer.add(layer,Color(100,200,100))
#    layer   = factory.createRingLayer(data,1,1,i)
#    viewer.add(layer,Color(50,100,50))

#ring = factory.createRing(data,0)
#viewer.add(ring,Color(100,100,200))

#ring = factory.createRing(data,1)
#viewer.add(ring,Color(100,200,100))

viewer.update()
