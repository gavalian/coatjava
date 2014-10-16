#===================================================================
# FULL geometry test
#===================================================================
from org.jlab.geom.detector.dc       import DCFactory
from org.jlab.geom.detector.ec       import ECFactory
from org.jlab.geom.detector.ftof     import FTOFFactory
from org.jlab.clas12.fastmc          import CLASFastMCSwimmer
from org.jlab.clas.physics  import Particle
from org.jlab.clas12.dbdata import DataBaseLoader
from java.lang              import Math

import random
import math
import sys
#===================================================================
#===================================================================
def getParticle(pid, mom, theta, phi):
    px = mom*Math.sin(theta)*Math.cos(phi)
    py = mom*Math.sin(theta)*Math.sin(phi)
    pz = mom*Math.cos(theta)
    particle = Particle(pid,px,py,pz,0.0,0.0,0.0)
    return particle

def getParticleDeg(pid, mom, theta,phi):
    theta_rad = Math.toRadians(theta)
    phi_rad   = Math.toRadians(phi)
    return getParticle(pid,mom,theta_rad,phi_rad)
#===================================================================
# MAIN program
#===================================================================

particleID  = sys.argv[1]
particleP   = sys.argv[2]
particleTh  = sys.argv[3]
particlePhi = sys.argv[4]

dataProvider = DataBaseLoader.getConstantsDC()
factory      = DCFactory()
dcDetector   = factory.createDetectorCLAS(dataProvider)


particle = getParticleDeg(int(particleID),float(particleP),float(particleTh),float(particlePhi))

print particle.toString()

swimmer = CLASFastMCSwimmer()
path    = swimmer.getParticlePath(particle)

print path.toString()

hitList = dcDetector.getHits(path)

print '\n\n'
print '=====|||  D E T E C T O R   H I T S |||=====\n\n'

for hit in hitList:
    print '\t',hit.toString()


print '\n\n\n'
