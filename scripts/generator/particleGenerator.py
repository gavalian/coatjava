from org.jlab.clas.physics   import *


nEvents = 15000
particles = []

particles.append(ParticleGenerator(   11,1.0,5.0,8.0,35.0, -15.0, 15.0))
particles.append(ParticleGenerator( -211,1.0,5.0,8.0,35.0, -15.0, 15.0))
#particles.append(ParticleGenerator( 2212,1.0,5.0,8.0,35.0, -15.0, 15.0))
#particles.append(ParticleGenerator(  321,1.0,5.0,8.0,35.0, -15.0, 15.0))
#particles.append(ParticleGenerator(  211,1.0,5.0,8.0,35.0,  45.0, 75.0))
#particles.append(ParticleGenerator( 2212,1.0,5.0,8.0,35.0,  45.0, 75.0))
#particles.append(ParticleGenerator(  321,1.0,5.0,8.0,35.0, -75.0, 45.0))

lundFile = open('lund_input.data','w')

event = PhysicsEvent()

for i in range(0,nEvents):
     event.clear()
     for pgen in particles:
          event.addParticle(pgen.getParticle())
          lundFile.write(event.toLundString())
          event.clear()

