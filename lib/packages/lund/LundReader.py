#
#
import re

class LundReader:
    def __init__(self,filename):
        self.lundFile   = open(filename,'r')
        self.readStatus = True

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

    def getEvent(self):
        return self.eventArray

    def getPidCount(self,pid):
        pcounter = 0
        for id in self.eventParticles:
            if(id==pid):
                pcounter = pcounter + 1
        return pcounter
    def getParticleCount(self):
        return len(self.eventParticles)

    def eventFilter(self,particles):
        pmap = {}
        for item in particles:
            if item in pmap:
                value = pmap[item]
                value = value + 1
                pmap[item] = value
            else:
                pmap[item] = 1

        #print pmap
        for key in pmap.keys():
            if(self.getPidCount(key)!=pmap[key]):
                return False
        return True

