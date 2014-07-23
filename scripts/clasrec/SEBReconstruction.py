#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from java.lang         import System
from java.lang         import String
from  org.jlab.evio.clas12  import EvioDataDictionary
from  org.jlab.evio.clas12  import EvioFactory
from  org.jlab.evio.clas12  import EvioSource
from  org.jlab.evio.clas12  import EvioDataBank
from  org.jlab.evio.clas12  import EvioDataSync
from  org.jlab.clas12.seb   import SEBReconstruction

#-----------------------------------------------------------
# Initilizing EvioSource object. It in turn initializes 
# EvioFactory which loads the dictionary from directory
# CLAS12DIR/lib/bankdefs/clas12
#-----------------------------------------------------------

inputFile = sys.argv[1]

writer = EvioDataSync()
writer.open('sebrec_output.evio')

reader = EvioSource()
reader.open(inputFile)

sebProc = SEBReconstruction()
sebProc.init()

icounter = 0
while(reader.hasEvent()):
    event = reader.getNextEvent()
    #event.show()
    sebProc.processEvent(event)
    writer.writeEvent(event)

print 'Events analyzed from File = ', icounter
writer.close()
