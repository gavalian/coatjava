
from org.jlab.detector.ftof import CLASFTOFDetector
from org.jlab.detector.cnd  import CLASCNDDetector
from org.jlab.detector.ec   import CLASECDetector
from org.jlab.detector.dc   import DCGeometry
from org.jlab.detector.ft   import CLASFTDetector
from org.jlab.detector.base import DetectorDescriptor
from org.jlab.geom  import Path3D,Face3D,Line3D,Point3D
import random
import math
from Particle import Particle

#================================================================
# exports hit information into a text file
#================================================================
def writeHitOutput(fo,hit):
    fo.write(str(hit.getDescriptor().getDetectorID()) + " ")
    fo.write(str(hit.getDescriptor().getSector()) + " ")
    fo.write(str(hit.getDescriptor().getSuperLayer()) + " ")
    fo.write(str(hit.getDescriptor().getLayer()) + " ")
    fo.write(str(hit.getDescriptor().getComponent()) + " ")
    fo.write(str(hit.position().x()) + " ")
    fo.write(str(hit.position().y()) + " ")
    fo.write(str(hit.position().z()) + " ")
    fo.write(" \n")

def writeHitArray(fo,hits):
    for hit in hits:
        writeHitOutput(fo,hit)
#================================================================
# End of routines
#================================================================

ftcal = CLASFTDetector()

path = Path3D()

output = file('detector_hits.data','w')

for i in range(1,200000):

    path.generateRandom(0.0,0.0,0.0,1.0,15.0,-180.0,180.0,3200,3)
    #-------------------------------------
    # determine hits in CND detector
    hits_ftcal = ftcal.getLayerHits(path)
    #print 'CND Hits size = ',hits_dc.size()
    writeHitArray(output,hits_ftcal)

print 'Finished....'
