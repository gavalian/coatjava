#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.bst  import BSTFactory
from org.jlab.clas12.dbdata      import DataBaseLoader
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

factory  = BSTFactory()
bstLayer = factory.createRingLayer(data,0,1,0)

ncomp = bstLayer.getNumComponents()

for i in range(0,256):
    line = bstLayer.getComponent(i).getLine()
    print 'COMPONENT ',i
    line.show()

