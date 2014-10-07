#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.visualizer    import CLASVisualizer
from org.jlab.geom.detector.ec   import ECFactory
from org.jlab.geom.detector.bst  import BSTFactory
from org.jlab.clas12.dbdata      import DataBaseLoader
from org.jlab.geom.prim          import Path3D,Face3D,Line3D,Point3D,Transformation3D
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

bstRing        = factory.createRingLayer(data,0,0,0)
bstRing_2_0    = factory.createRingLayer(data,0,0,0)
bstRing_2_1    = factory.createRingLayer(data,0,0,0)

bstRing_0_0    = factory.createRingLayer(data,0,0,0)
bstRing_0_1    = factory.createRingLayer(data,0,0,0)

bstRingUp      = factory.createRingLayer(data,0,0,0)
bstRingDown    = factory.createRingLayer(data,0,1,0)

bstTransform   = factory.getDetectorTransform(data)

bstRing_2_0.setTransformation(bstTransform.get(2,0,0))
bstRing_2_1.setTransformation(bstTransform.get(2,0,1))

bstRing_0_0.setTransformation(bstTransform.get(0,0,0))
bstRing_0_1.setTransformation(bstTransform.get(0,0,1))

viewer = CLASVisualizer(100,100,1400,1200)

viewer.setBackgroundColor(Color(150,150,255))
viewer.getDisplay().setBackgroundColor(Color(150,150,255))
viewer.setVisible(True)
#viewer.setTransparancy(0.5)

viewer.add(bstRingUp.getBoundary(),Color(100,100,255))
#viewer.add(bstRingDown,Color(100,100,155))

boundary = bstRing_2_0.getBoundary()
boundary.show()
#viewer.add(boundary,Color(100,100,155))
#viewer.add(bstRing_2_1,Color(100,100,155))

#viewer.add(bstRing_0_0,Color(100,100,155))
#viewer.add(bstRing_0_1,Color(100,100,155))

viewer.update()
