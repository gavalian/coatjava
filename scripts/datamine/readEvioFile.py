#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from java.lang         import System
from java.lang         import String
from org.jlab.evio.clas12  import EvioDataDictionary, EvioFactory, EvioSource, EvioDataBank

#-----------------------------------------------------------
# Initilizing EvioSource object. It in turn initializes 
# EvioFactory which loads the dictionary from directory
# CLAS12DIR/lib/bankdefs/clas12
#-----------------------------------------------------------

filename = sys.argv[1]

reader = EvioSource()
reader.open(filename)

icounter = 0
while(reader.hasEvent()):
    event = reader.getNextEvent()
    #event.show()
    if(event.hasBank('CLAS6EVENT::particle')==True):
        bankP = event.getBank('CLAS6EVENT::particle')
        bankD = event.getBank('CLAS6EVENT::detector')
        bankP.show()
        bankD.show()
        pid = bankP.getInt('pid')
        px  = bankP.getFloat('px')
        py  = bankP.getFloat('py')
        pz  = bankP.getFloat('pz')
        print '----------> printing particles'
        for i in range(0,len(pid)):
            print pid[i],px[i],py[i],pz[i]

    icounter = icounter + 1

print 'Events analyzed from File = ', icounter
