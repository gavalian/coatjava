#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.ec    import ECFactory
from org.jlab.geom.detector.ftof  import FTOFFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from java.lang import Math
import random
import math
import sys

#===================================================================
# 
#===================================================================

data = DataBaseLoader.getConstantsFTOF()
print data.toString()

factory = FTOFFactory()
ftofDetector   = factory.createDetectorLocal(data)
#ecDetector.show()
layerA = ftofDetector.getSector(0).getSuperlayer(0).getLayer(0)

for c in range(0,layerA.getNumComponents()):
    comp = layerA.getComponent(c)
    mp   = comp.getMidpoint()
    print 'COMP ',c, mp.toString()
