#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.ec   import ECFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from java.lang import Math
from org.jlab.geom.gui import GeometryFrame 
import random
import math
import sys

#===================================================================
# 
#===================================================================
data = DataBaseLoader.getCalorimeterConstants()

factory = ECFactory()
ecDetector   = factory.createDetectorCLAS(data)
ecDetector.show()

ecSuperlayer = factory.createSuperlayer(data,0,0)

xdata = [0.0,1.0,2.0,3.0,4.0]
ydata = [0.0,1.0,2.0,3.0,4.0]

plotter = GeometryFrame(800,800,300.0,300.0)
plotter.addLineXY(Line3D(0.,0.,0.,100.0,100.0,0.0))

for i in range(0,ecSuperlayer.getNumLayers()):
    layer = ecSuperlayer.getLayer(i)
    ncomp = layer.getNumComponents()
    for c in range(0,ncomp):
        line = layer.getComponent(c).getLine()
        if(i==0 or i==1 or i==2):
            plotter.addLineXY(line)
        line.show()

plotter.setVisible(True)
