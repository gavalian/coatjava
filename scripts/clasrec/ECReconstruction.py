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
from  org.jlab.rec.ftof     import FTOFReconstruction
from  org.jlab.rec.ec       import ECReconstruction
from  org.jlab.clas12.utils import Benchmark

#-----------------------------------------------------------
# Initilizing EvioSource object. It in turn initializes 
# EvioFactory which loads the dictionary from directory
# CLAS12DIR/lib/bankdefs/clas12
#-----------------------------------------------------------

inputFile = sys.argv[1]

writer = EvioDataSync()
writer.open('ec_reconstruction_output.evio')

reader = EvioSource()
reader.open(inputFile)

ecProc = ECReconstruction()
ecProc.init()
bench = Benchmark()
bench.addTimer('reader')
bench.addTimer('ecrec')
bench.addTimer('total')

bench.resume('total')

icounter = 0
while(reader.hasEvent()):
    bench.resume('reader')
    event = reader.getNextEvent()
    bench.pause('reader')
    #print '----> processing the event ------------------------------------'
    bench.resume('ecrec')
    ecProc.processEvent(event)
    bench.pause('ecrec')
    writer.writeEvent(event)

print 'Events analyzed from File = ', icounter
writer.close()
bench.pause('total')
print '\n','\n',bench.toString()

