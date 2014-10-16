#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.bst  import BSTFactory
from org.jlab.clas12.dbdata      import DataBaseLoader
from org.jlab.geom.gui           import GeometryFrame
#===================================================================
# Geometry primitives
#===================================================================
from org.jlab.geom.prim import Path3D
from org.jlab.geom.prim import Face3D
from org.jlab.geom.prim import Line3D
from org.jlab.geom.prim import Point3D
from org.jlab.geom.prim import Transformation3D
#===================================================================
from java.lang import Math
import random
import math
import sys

#===================================================================
# Geometry Package Tests for BST detector
#===================================================================

data = DataBaseLoader.getConstantsBST()
print data.toString()

factory   = BSTFactory()

bstLayer0 = factory.createRingLayer(data,0,0,0)
bstLayer1 = factory.createRingLayer(data,0,0,1)

frame = GeometryFrame(800,800,10,40);
frame.setVisible(True)

for i in range(0,256):
    line = bstLayer1.getComponent(i).getLine()
    line.show()
    if i%4==0:
        frame.addLineXZ(line)
