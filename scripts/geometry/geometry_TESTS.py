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

for sl in range(0,6):
	for l in range(0,6):
		layer = dcDET.getSector(0).getSuperlayer(sl).getLayer(l)
		ncomp = layer.getNumComponents()
		print '**************** SUPERLAYER ',sl,' ********** LAYER ',l,' **********'
		for comp in range(0,ncomp):
			point = layer.getComponent(comp).getMidpoint()
			print '%3d %3d %5d %12.5f %12.5f %12.5f' % (sl,l,comp,point.x(),point.y(), point.z())


