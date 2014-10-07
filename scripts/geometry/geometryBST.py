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
bstLayer = factory.createRingLayer(data,0,0,0)


sectorMap = {0:10,1:14,2:18,3:24}

transform = factory.getDetectorTransform(data)

for sec in range(0,4):
    nlayers = sectorMap[sec]
    for supl in range(0,2):
        print ' sector = ',sec, '  superlayer = ', supl, '  nlayers = ',nlayers
        for layer in range(0,nlayers):
            print ' sector = ',sec, '  superlayer = ', supl, ' layer = ',layer
            tr = transform.get(sec,supl,layer)
            tr.show()


#-------------------------------------------------------------------
# Use the transformation to get wire positions for 
# sector 2 superlayer 1 and layer 8
#-------------------------------------------------------------------

ncomp = bstLayer.getNumComponents()
for i in range(0,256):
    line = bstLayer.getComponent(i).getLine()
    print 'COMPONENT ',i
    line.show()
    tr = transform.get(2,1,8)
    nline = Line3D()
    nline.copy(line)
    tr.apply(nline)
    nline.show()

    
