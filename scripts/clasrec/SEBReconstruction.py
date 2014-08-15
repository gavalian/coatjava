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
from  org.jlab.rec.sc       import SCReconstruction
from  org.jlab.rec.ec       import ECReconstruction
from  org.jlab.clas12.utils import Benchmark

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

#------------------------------------------------------------
# initializing the components to run on the simulation file
#------------------------------------------------------------
ftofProc = SCReconstruction()
ftofProc.init()

ecProc   = ECReconstruction()
ecProc.init()

sebProc  = SEBReconstruction()
sebProc.init()
#------------------------------------------------------------
# Initializing the benchmark timers
#------------------------------------------------------------
bench = Benchmark()
bench.addTimer('reader')
bench.addTimer('ecrec')
bench.addTimer('screc')
bench.addTimer('sebrec')
bench.addTimer('total')

#------------------------------------------------------------

icounter = 0
while(reader.hasEvent()):

    bench.resume('total')

    bench.resume('reader')
    event = reader.getNextEvent()
    bench.pause('reader')
    #event.show()

    bench.resume('screc')
    ftofProc.processEvent(event)
    bench.pause('screc')

    bench.resume('ecrec')
    ecProc.processEvent(event)
    bench.pause('ecrec')

    #if(event.hasBank('FTOFRec::ftofhits')):
    #    print '>>>>>>>>>>>>>> found bank FTOFRec::ftofhits'
    #if(event.hasBank('ECRec::clusters')):
    #    print '>>>>>>>>>>>>>> found bank ECREC'

    bench.resume('sebrec')
    sebProc.processEvent(event)
    bench.pause('sebrec')

    writer.writeEvent(event)
    bench.pause('total')

#------------------------------------------------------------
print 'Events analyzed from File = ', icounter
writer.close()
print '\n','\n',bench.toString()
