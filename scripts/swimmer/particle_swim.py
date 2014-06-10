#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from java.lang         import System
from java.lang         import String
from java.io           import File
from  cnuphys.magfield import Torus
from  cnuphys.swim     import Swimmer,DefaultSwimStopper,DefaultListener
#-----------------------------------------------------------
# This is an example on how to use swimmer package
#-----------------------------------------------------------

torusFile = File('../../lib/data/magfield/clas12-fieldmap-torus.dat')
torus     = Torus.fromBinaryFile(torusFile)

swimmer =  Swimmer(torus)

xo = 0.0
yo = 0.0
zo = 0.0

theta = 30.0
phi   =  0.0

rmax  = 6.0
maxpath = 8.0

momentum = 3.0
stepSize = 0.005

hdata = [0.0,0.0,0.0]

stopper  = DefaultSwimStopper(rmax)
listener = DefaultListener()
nsteps   = swimmer.swim(-1, xo, yo, zo, momentum,theta, phi, stopper, listener, maxpath, stepSize)

print ' steps = ', nsteps

traj = swimmer.swim(-1, xo, yo,zo, momentum, theta, phi, stopper, maxpath, stepSize,Swimmer.CLAS_Tolerance, hdata)

print 'aduptive swimming test.', traj
for item in traj:
    print item
