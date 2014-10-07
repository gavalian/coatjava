#*****************************************************************
# Particle class for event filtering
#*****************************************************************
#*****************************************************************
from math import sqrt,acos,atan2

class Particle:
    def __init__(self):
        self.ppid  = 11
        self.ppx   = 0.0
        self.ppy   = 0.0
        self.ppz   = 0.0
        self.pmass = 0.0

    def set(self,id,px,py,pz):
        self.ppid = id
        self.ppx  = px
        self.ppy  = py
        self.ppz  = pz

    def theta(self):
        if(self.mag()==0):
            return 0.0
        return acos(self.ppz/self.mag())

    def phi(self):
        return atan2(self.ppy,self.ppx)

    def mag(self):
        return sqrt(self.ppx*self.ppx+self.ppy*self.ppy+self.ppz*self.ppz)
