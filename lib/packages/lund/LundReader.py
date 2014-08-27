#
#
import re

class LundReader:
    def __init__(self,filename):
        self.lundFile = open(filename,'r')

    def readEvent(self):
        header = self.lundFile.readline()
        words  = header.split()
        nrows  = int(words[0])
        self.eventArray = []
        self.eventParticles = []
        self.eventArray.append(header)
        for i in range (0,nrows):
            line = self.lundFile.readline()
            self.eventArray.append(line)
            linewords = line.split()
            if(int(linewords[2])==1):
                self.eventParticles.append(int(linewords[3]))

        #for line in self.eventArray:
        #    print line,
        print '---> ', self.eventParticles

    def getEvent(self):
        return self.eventArray

    def getPidCount(self,pid):
        pcounter = 0
        for id in self.eventParticles:
            if(id==pid):
                pcounter = pcounter + 1
        return pcounter
