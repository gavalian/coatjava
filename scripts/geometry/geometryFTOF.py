from org.jlab.clas12.dbdata import DataBaseLoader
from org.jlab.geom.detector.ftof import FTOFFactory
import random
import math
from Particle import Particle


sec_id = 0
spl_id = 0
lyr_id = 0

dataProvider = DataBaseLoader.getTimeOfFlightConstants()
print dataProvider.toString()

factory  = FTOFFactory()
#sector   = factory.makeSector(dataProvider,0)
detector = factory.makeDetector(dataProvider)

detector.show()

print 'FTOF detector      SECTORS = ',detector.getNumSectors()

sector = detector.getSector(sec_id)

print 'FTOF sector 0  SUPERLAYERS = ', sector.getNumSuperLayers()

superlayer = sector.getSuperLayer(spl_id)

print 'FTOF sector 0       LAYERS = ', superlayer.getNumLayers()

layer = superlayer.getLayer(lyr_id)

print 'FTOF sector 0      SENSORS = ', layer.getNumSensors()

for i in range(0,layer.getNumSensors()):
    print ' sensor ',i,' midpoint = ',layer.getSensor(i).getMidpoint(),
    print '   direction ',i,' midpoint = ',layer.getSensor(i).getDirection(),

