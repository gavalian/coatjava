#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from java.lang         import System
from java.lang         import String
from   org.jlab.evio.clas12  import EvioDataDictionary, EvioFactory

#-----------------------------------------------------------
# loading the dictionary from current directory.
# and printing descriptors that were loaded
#-----------------------------------------------------------
EvioFactory.loadDictionary('.')
EvioFactory.getDictionary().show()

#-----------------------------------------------------------
# showing detialed description of CUSTOM:dgtz descriptor
#-----------------------------------------------------------

EvioFactory.getDictionary().getDescriptor('CUSTOM::dgtz').show()

#-----------------------------------------------------------
# Create a bank for descriptor CUSTOM::dgtz with 5 rows
# and print the content of the bank.
#-----------------------------------------------------------
bankDGTZ = EvioFactory.createBank('CUSTOM::dgtz',5)
bankDGTZ.show()

bankTRUE = EvioFactory.createBank('CUSTOM::true',5)
bankTRUE.show()

#-----------------------------------------------------------
# Changing the values in the bank and displaying bank
# content.
#-----------------------------------------------------------

bankDGTZ.setInt('nhit',0,1)
bankDGTZ.setInt('nhit',1,2)
bankDGTZ.setInt('nhit',2,3)

bankDGTZ.setInt('ADC',0,1200)
bankDGTZ.setInt('ADC',1,1400)
bankDGTZ.setInt('ADC',2,1500)

bankDGTZ.setInt('TDC',0,4600)
bankDGTZ.setInt('TDC',1,6700)
bankDGTZ.setInt('TDC',2,4600)

bankDGTZ.show()
