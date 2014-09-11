#***********************************************************************
# Simple Lund text file reader. allows checking final state of the 
# read event.
#***********************************************************************

import re
from   Particle import Particle

class LundReader:
    #------------------------------------------------------------------
    # Default constructor with file name to open
    #------------------------------------------------------------------
    def __init__(self,filename):
        self.lundFile   = open(filename,'r')
        self.readStatus = True
    #------------------------------------------------------------------
    # Reads next event in the file, returns true if the event is fully
    # read. 
    #------------------------------------------------------------------
    def readEvent(self):
        if(self.readStatus==False):
            print '[LundReader] -------> end of file reached'
            return self.readStatus

        header = self.lundFile.readline()
        if(len(header)<5):
            self.readStatus = False
            return self.readStatus

        words  = header.split()
        nrows  = int(words[0])
        self.eventArray = []
        self.eventParticles = []
        self.eventArray.append(header)
        for i in range (0,nrows):
            line = self.lundFile.readline()
            if(len(line)<10):
                self.eventArray = []
                self.eventParticles = []
                self.readStatus = False
                return self.readStatus

            self.eventArray.append(line)
            linewords = line.split()
            if(int(linewords[2])==1):
                self.eventParticles.append(int(linewords[3]))
        return self.readStatus
        #for line in self.eventArray:
        #    print line,
        #print '---> ', self.eventParticles
    #------------------------------------------------------------------
    # returns an array of the text for the event exactly as it was
    # read from input file. this array can be written into output
    #------------------------------------------------------------------
    def getEvent(self):
        return self.eventArray
    #------------------------------------------------------------------
    # Returns number of particles with given pid
    #------------------------------------------------------------------
    def getPidCount(self,pid):
        pcounter = 0
        for id in self.eventParticles:
            if(id==pid):
                pcounter = pcounter + 1
        return pcounter
    #------------------------------------------------------------------
    # returns number of particles in the final state
    #------------------------------------------------------------------
    def getParticleCount(self):
        return len(self.eventParticles)

    #------------------------------------------------------------------------------
    # Checks if the event matches given pattern
    #------------------------------------------------------------------------------
    def eventFilter(self,particles,exclusive):
        nparticles = 0
        pmap = {}
        for item in particles:
            nparticles = nparticles + 1
            if item in pmap:
                value = pmap[item]
                value = value + 1
                pmap[item] = value
            else:
                pmap[item] = 1

        if(exclusive==True):
            if(self.getParticleCount()!=nparticles):
                return False

        for key in pmap.keys():
            if(self.getPidCount(key)!=pmap[key]):
                return False
        return True
    #------------------------------------------------------------------------------
    # returns particle with given particle ID
    #------------------------------------------------------------------------------
    def getParticle(self,id):
        par = Particle()
        icounter = 0
        for line in self.eventArray:
            items = line.split()
            #print '--> items printout' ,items
            if(icounter!=0):
                if(int(items[2])==1 and int(items[3])==id):
                    par.set(id,float(items[6]),float(items[7]),float(items[8]))
            icounter = icounter + 1
        return par
    #------------------------------------------------------------------------------
    # END of CLASS LUNDREADER
    #------------------------------------------------------------------------------
