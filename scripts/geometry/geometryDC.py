from org.jlab.geom.prim  import Path3D,Face3D,Line3D,Point3D,Transformation3D
from org.jlab.geom.detector.ec   import ECFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.detector.dc       import DCFactory
import random
import math


rootVolume  = Point3D(2170.0799,0.0,6789.8397)
layerVolume = Point3D(0.0,0.0,-9.03)
paddle      = Point3D(-0.668675418863381,0,0)

dataDC  = DataBaseLoader.getConstantsDC()
factory = DCFactory()
#dcDET   = factory.createDetectorCLAS(dataDC)
dcDET   = factory.createDetectorTilted(dataDC)

adjust = [-90.0,90.0,-90.0,-90.0,-90.0,-90.0]

for sl in range(0,6):
	layer = dcDET.getSector(0).getSuperlayer(sl).getLayer(0)
	ncomp = layer.getNumComponents()
	#print '**************** SUPERLAYER ',sl,' ********** LAYER ',0,' **********'
	dir  = layer.getComponent(5).getDirection()
	#line = layer.getComponent(5).getLine()
	print 'SUPERLAYER = ', sl, ' DIR = ', dir.phi()*57.29, dir.phi()*57.29-adjust[sl]
	#line.show()

