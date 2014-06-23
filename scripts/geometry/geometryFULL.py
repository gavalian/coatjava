
from org.jlab.detector.ftof import CLASFTOFDetector
from org.jlab.detector.cnd  import CLASCNDDetector
from org.jlab.detector.ec   import CLASECDetector
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

ftof = CLASFTOFDetector()
ec   = CLASECDetector()
cnd  = CLASCNDDetector()

ftof.initXML('../../lib/geometry/FTOFPaddles_CLAS.xml')

path = Path3D()

output = file('detector_hits.data','w')

for i in range(1,2000):

    path.generateRandom(0.0,0.0,0.0,10.0,135.0,-5.0,5.0,3200,3)
    #-------------------------------------
    # determine hits in CND detector
    hits_cnd = cnd.getLayerHits(path)
    print 'CND Hits size = ',hits_cnd.size()
    #-------------------------------------
    # determine hits in EC (and PCAL)
    hits_ec  = ec.getLayerHits(path)
    print 'EC Hits size = ',hits_ec.size()

print 'Finished....'
