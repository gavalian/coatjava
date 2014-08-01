#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.visualizer    import CLASVisualizer
from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from java.lang import Math
from java.awt import Color
import random
import math
import sys

#===================================================================
# 
#===================================================================

viewer = CLASVisualizer()
viewer.setVisible(True)

path = Path3D()
path.addPoint(0.0,0.0,0.0)
path.addPoint(300.0,400.0,200.0)

viewer.add(path,Color.WHITE)
viewer.update()
