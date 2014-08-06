#===========================================================
# Example script that produces the geometry file for GEMC.
# This module is for producing FTOF geometry.
#
# Author: G. Gavalian (8/5/2014)
#===========================================================
from org.jlab.geom.detector.ftof  import FTOFFactory
from org.jlab.clas12.dbdata       import DataBaseLoader
from org.jlab.geom.prim           import Transformation3D
#-----------------------------------------------------------
# Create a data provider which loads the data from the 
# database. The database is a CCDB implementation located
# on the host clasdb.jlab.org
#
# The data provider is passed to the factory to create a 
# detector (FTOF detector in this case) in local coordinates
#-----------------------------------------------------------
data     = DataBaseLoader.getConstantsFTOF()
factory  = FTOFFactory()
detector = factory.createDetectorCLAS(data)

for i in range(0,6):

    layerA = detector.getSector(i).getSuperlayer(0).getLayer(0)
    layerAL = factory.createLayer(data,0,0,0)

    numComponents = layerAL.getNumComponents()

    midpFirst = layerAL.getComponent(0).getMidpoint()
    midpLast  = layerAL.getComponent(numComponents-1).getMidpoint()    
    transform = layerAL.getTransformation()
    transinv  = transform.inverse()
    transform.show()
    transinv.show()
    
    dshift = (midpLast.x()-midpFirst.x())/2.0
    moveShift = dshift-midpLast.x()
    print 'the shift = ',moveShift,dshift,midpFirst.x(),midpLast.x()
    moveLayer = Transformation3D().translateXYZ(moveShift,0.0,0.0)
    layerAL.setTransformation(moveLayer)

    for p in range(0,numComponents):
        shape    = layerAL.getComponent(p).getVolumeShape()
        midpoint = layerAL.getComponent(p).getMidpoint() 
        pLength  = shape.face(0).point(1).y()-shape.face(0).point(0).y()
        pHeight  = shape.face(0).point(2).x()-shape.face(0).point(1).x()
        pWidth   = shape.face(2).point(2).z()-shape.face(2).point(1).z()
        print 'position = ','0.0*cm ',midpoint.y(),'*cm ',midpoint.x()/2.54,'*cm ',' dim = ', pLength/2.0/2.54,'*cm ',
        print pHeight/2.0/2.54,'*cm ',pWidth/2.0/2.54,'*cm'
        #shape.show()
        
