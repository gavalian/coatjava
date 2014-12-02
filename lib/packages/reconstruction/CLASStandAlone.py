#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
import sys
import getopt
import glob
from java.lang         import System
from java.lang         import String
from  org.jlab.clas12.seb   import SEBReconstruction
from  org.jlab.rec.eb       import CLASEventBuilder
from  org.jlab.rec.sc       import SCReconstruction
from  org.jlab.rec.ec       import ECReconstruction
from  org.jlab.rec.bst.services  import BSTReconstruction
from  org.jlab.clas12.base  import CLASRecStandalone
from  org.jlab.rec.bst.services   import BSTReconstruction
from  org.jlab.rec.dc.services import HitBasedTracking
from  org.jlab.rec.dc.services import TimeBasedTracking
from  org.jlab.rec.dc          import Constants
from  org.jlab.clas12.seb   import SEBEventBuilderDebug
#-----------------------------------------------------------
# Initilizing EvioSource object. It in turn initializes 
# EvioFactory which loads the dictionary from directory
# CLAS12DIR/lib/bankdefs/clas12
#-----------------------------------------------------------

def printUsage():
    print '*******************************************'
    print '*   C L A S 12  RECONSTRUCTION SCRIPT     *'
    print '*******************************************'
    print '\n\n'
    print '\t Usage : runReconstruction inputfile.evio -[flags]'
    print '\n'
    print 'Options: \n'
    print '\t-o file : output file name'
    print '\t-n num  : number of events to reconstruct'
    print '\t-e evt  : reconstruct one event with EVT NUM = evt (bank 10 evio)'
    print '\t-s LIST : list of reconstruction Modules to run (ALL=DC:FTOF:EC:HTCC)'
    print '\n\n'
    print 'Flags: \n'
    print '\t-r : run reconstruction with reversed field'
    print '\n\n'
    print 'Examples: '
    print '\nTo run DC and FTOF reconstruction for 300 events on generated file use:'
    print '\n\t>runReconstruction input.evio -s DC:FTOF -n 300'
    print '\n\n'


#-----------------------------------------------------------------------------------
# MAIN PROGRAM BODY
#-----------------------------------------------------------------------------------

if(len(sys.argv)<2):
    printUsage()
    sys.exit()

inputFile  = sys.argv[1]
outputFile = "rec_output.evio"
services   = []
recNumEvents  = -1
recEvent      = -1

optlist,args = getopt.getopt(sys.argv[2:],'n:o:e:s:r')
#===================================================
# parse options
#===================================================
print optlist

reversedFiled = False

for o,a in optlist:
    print 'o = ',o,' a = ',a
    if o in "-n":
        #clasREC.setEventRange(0,int(a))
        recNumEvents = int(a)
    if o in "-e":
        recNumEvents = -1
        recEvent     = int(a)
        #clasREC.setEventRange(0,-1)
        #clasREC.setRecEvent(int(a))
    if o in "-o":
        outputFile = a
    if o in "-s":
        services = a.split(':')
    if o in "-r":
        reversedFiled = True

clasREC = CLASRecStandalone(inputFile)
clasREC.setOutputFile(outputFile)
clasREC.setEventRange(0,recNumEvents)
clasREC.setRecEvent(recEvent)

#===================================================
# Add services to reconstruction 
#===================================================

if len(services)<1:
    services = ['DC','BST','FTOF','EC','EB']

print 'Running Services : ', services

for item in services:
    if item=='DC':
        if reversedFiled==True:
            Constants.reverseTorus = True
            print '\n\n=====> switching to reverse Filed\n\n'
        dcRecHB = HitBasedTracking()
        dcRecTB  = TimeBasedTracking()
        clasREC.add(dcRecHB)
        clasREC.add(dcRecTB)
    if item=='FTOF':
        scRec = SCReconstruction()
        clasREC.add(scRec)
    if item=='EC':
        ecRec    = ECReconstruction()
        clasREC.add(ecRec)

    if item=='BST':
        bstRec    = BSTReconstruction()
        clasREC.add(bstRec)

    if item=='BST':
        bstRec   = BSTReconstruction()
        clasREC.add(bstRec)
    if item=='EB':
        clasEB   = CLASEventBuilder()
        clasREC.add(clasEB)
    if item=='DEBUG':
        clasDebug = SEBEventBuilderDebug()
        clasREC.add(clasDebug)

clasREC.run()

#dcRecHB  = HitBasedTracking()
#dcRecTB  = TimeBasedTracking()
#scRec    = SCReconstruction()
#ecRec    = ECReconstruction()
#sebRec   = SEBReconstruction()
#sebDebug = SEBEventBuilderDebug()
#clasEB   = CLASEventBuilder()
#clasREC.add(dcRecHB)
#clasREC.add(dcRecTB)
#clasREC.add(scRec)
#clasREC.add(ecRec)
#clasREC.add(sebDebug)
#clasREC.add(sebRec)
#clasREC.add(clasEB)


