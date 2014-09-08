#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from java.lang         import System
from java.lang         import String
from  org.jlab.clas12.seb   import SEBReconstruction
from  org.jlab.rec.eb       import CLASEventBuilder
from  org.jlab.rec.sc       import SCReconstruction
from  org.jlab.rec.ec       import ECReconstruction
from  org.jlab.clas12.base  import CLASRecStandalone
from  org.jlab.rec.dc.services import HitBasedTracking
from  org.jlab.rec.dc.services import TimeBasedTracking
from  org.jlab.rec.dc          import Constants
from  org.jlab.clas12.seb   import SEBEventBuilderDebug
#-----------------------------------------------------------
# Initilizing EvioSource object. It in turn initializes 
# EvioFactory which loads the dictionary from directory
# CLAS12DIR/lib/bankdefs/clas12
#-----------------------------------------------------------

inputFile = sys.argv[1]

clasREC = CLASRecStandalone(inputFile)

dcRecHB  = HitBasedTracking()
dcRecTB  = TimeBasedTracking()
scRec    = SCReconstruction()
ecRec    = ECReconstruction()
sebRec   = SEBReconstruction()
sebDebug = SEBEventBuilderDebug()
clasEB   = CLASEventBuilder()

Constants.useKalmanFilter = False

clasREC.add(dcRecHB)
clasREC.add(dcRecTB)
clasREC.add(scRec)
clasREC.add(ecRec)
clasREC.add(sebDebug)
#clasREC.add(sebRec)
clasREC.add(clasEB)

clasREC.run()
