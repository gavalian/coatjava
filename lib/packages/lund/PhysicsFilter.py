from LundReader import LundReader
import sys
import getopt
import glob


def printUsage():
    print '*****************************************************************'
    print '*   L U N D  event filtering program (clas12 physics package)   *'
    print '*****************************************************************'
    print '\n\n'
    print '\t Usage : python PhysicsFilter.py -f filename.data -p [particle list ":" separated] [flags]'
    print '\n'
    print 'Options: \n'
    print '\t-f file : file name to filter'
    print '\t-d dir  : directory name where lund files are located (*.data files will be processed)'
    print '\t-p list : particle list ":" separated (i.e. 11:2212:211:-211)'
    print '\t-e      : switch on exlusive flag (default is inclusive)'
    print '\n\n'
    print 'Examples: '
    print '\nTo select events of inclusive pi0 production on proton use:'
    print '\n\t>python PhysicsFilter.py -f file.data -p 11:2212:22:22'
    print '\nTo select events of exclusive phi meson production on proton use:'
    print '\n\t>python PhysicsFilter.py -f file.data -p 11:2212:321:-321 -e'
    print '\n\n'

def processFiles(fileList,evPattern,exFlag):
    fileWrite = open('lund_output.data','w')
    fcounter = 0
    nfiles   = len(fileList)
    for file in fileList:
        print '[process-filter]---> openning file [',fcounter,'/',nfiles,']',file
        print '[process-filter]---> processing with flag exc =',exFlag
        fcounter = fcounter + 1
        reader = LundReader(file)
        icounter  = 0
        ifiltered = 0
        while(reader.readEvent()):
            icounter = icounter + 1
            flagElectron = True
            #electron = reader.getParticle(11)
            #if(electron.mag()>0.5 and electron.theta()*57.29>8.0 and electron.theta()*57.29<35.0):
            #    flagElectron = True

            if(reader.eventFilter(evPattern,exFlag)==True and flagElectron==True):
                ifiltered = ifiltered + 1
                event = reader.getEvent()
                #par   = reader.getParticle(11)
                #print par.mag(),par.theta(),par.phi()
                for line in event:
                    fileWrite.write(line)

        print '[process-filter]---> summary ::  events = ',icounter,'  filtered = ',ifiltered
        #----------------------------

#------------------------------------------------------------------------------------
#_______ MAIN __________
#------------------------------------------------------------------------------------
# Program filters events in the Lund file according to the pattern given in
# the command line
#------------------------------------------------------------------------------------


optlist,args = getopt.getopt(sys.argv[1:],'f:d:p:em:')

processFileList    = []
processEventFilter = []
processExclusive   = False
 
for o,a in optlist:
    if o in "-f":
        processFileList = [a]
    if o in "-d":
        processFileList = glob.glob(a+'/*.dat')
    if o in "-p":
        processEventFilter = a.split(':')
    if o in "-e":
        processExclusive = True

if(len(processFileList)<1 or len(processEventFilter)<1):
    printUsage()
    exit()

eventFilter = []
for item in processEventFilter:
    eventFilter.append(int(item))

#print 'processing files = ',processFileList
#print 'filter  = ',processEventFilter

processFiles(processFileList,eventFilter,processExclusive)



