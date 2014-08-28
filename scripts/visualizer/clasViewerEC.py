#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.visualizer    import CLASVisualizer
from org.jlab.geom.detector.ec  import ECFactory
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

data = DataBaseLoader.getConstantsEC()
print data.toString()

factory = ECFactory()
ecDetector = factory.createSuperlayer(data,0,0)

viewer = CLASVisualizer(100,100,1400,1200)
viewer.setBackgroundColor(Color(150,150,255))
viewer.getDisplay().setBackgroundColor(Color(150,150,255))
viewer.setVisible(True)
viewer.setTransparancy(0.5)

viewer.add(ecDetector,Color(200,200,255))

viewer.update()
