#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from java.lang         import System
from java.lang         import String
from   org.jlab.evio.clas12  import EvioDataDictionary, EvioFactory, EvioSource, EvioDataBank

#-----------------------------------------------------------
# Initilizing EvioSource object. It in turn initializes 
# EvioFactory which loads the dictionary from directory
# CLAS12DIR/lib/bankdefs/clas12
#-----------------------------------------------------------

reader = EvioSource()
reader.open('../../lib/data/ftof_1Kevents.evio')

icounter = 0
while(reader.hasEvent()):
    event = reader.getNextEvent()
    event.show()
    bank = event.getBank('FTOF1A::dgtz')
    print 'BANK rows = ', bank.rows()
    bank.show()
    if(bank.rows()>0):
        for i in range(0,bank.rows()):
            print bank.getInt('ADCL')[i]
    icounter = icounter + 1

print 'Events analyzed from File = ', icounter
