from org.jlab.clas12.fastmc import CLASFastMCSwimmer
from org.jlab.clas.physics  import Particle

swimmer  = CLASFastMCSwimmer()
particle = Particle(11,0.5,0.0,1.4,0.0,0.0,0.0)
path     = swimmer.getParticlePath(particle)
