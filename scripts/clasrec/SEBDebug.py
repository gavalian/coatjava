#=====================================================================
# A python module that implements a Java interface to
# create a building object
#=====================================================================
import sys
from org.jlab.geom.detector.dc  import DCFactory
from org.jlab.clas12.dbdata import DataBaseLoader
from java.lang         import System
from java.lang         import String
from  org.jlab.clas.physics  import Particle,Vector3
from  org.jlab.clas12.utils  import Benchmark
from  org.jlab.clas12.fastmc import CLASRotatedSwimmer
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


dataProvider = DataBaseLoader.getConstantsDC()
factory      = DCFactory()
dcDetector   = factory.createDetectorTilted(dataProvider)

writer = EvioDataSync()
writer.open('sebrec_output.evio')

reader = EvioSource()
reader.open(inputFile)

swimmer = CLASRotatedSwimmer()

icounter = 0
while(reader.hasEvent()):

    icounter = icounter + 1
    if(icounter%100==0):
        print 'process counter = ',icounter
    event = reader.getNextEvent()

    pid = event.getInt(20,1)
    px  = event.getDouble(20,2)
    py  = event.getDouble(20,3)
    pz  = event.getDouble(20,4)
    bankSEBDC = event.getDictionary().createBank('SEBDebug::dc',36)
    if pid != None:
        #print len(pid)
        part = Particle(pid[0],px[0]/1000.0,py[0]/1000.0,pz[0]/1000.0,0.0,0.0,0.0)
        #print part.toString()
        for superlayer in range(0,6):
            for layer in range(0,6):
                dcLayer = dcDetector.getSector(0).getSuperlayer(superlayer).getLayer(layer)
                plane   = dcLayer.getPlane()
                zt      = plane.point().z()/100.0
                #print 'super = ',superlayer,' layer = ', layer , ' z = ', plane.point().z()
                result = swimmer.getTrackParameters(part,zt)
                #print result
                row = superlayer*6 + layer
                bankSEBDC.setInt('sector',row,0)
                bankSEBDC.setInt('layer',row,row)
                bankSEBDC.setDouble('X',row,result[0])
                bankSEBDC.setDouble('Y',row,result[1])
                bankSEBDC.setDouble('Z',row,result[2])
                bankSEBDC.setDouble('uX',row,result[3])
                bankSEBDC.setDouble('uY',row,result[4])
                bankSEBDC.setDouble('uZ',row,result[5])
        event.appendBanks(bankSEBDC)
        writer.writeEvent(event)
        #bankSEBDC.show()

writer.close()
#vec = Vector3()
#vec.setMagThetaPhi(2.5,15.0/57.29,0.0)
#electron = Particle(11,vec.x(),vec.y(),vec.z(),0.0,0.0,0.0)
#print electron.toString()
#for i in range(0,10):
#    zt = 1.5 + 0.5*i
#    result = swimmer.getTrackParameters(electron,zt)
#    print result
