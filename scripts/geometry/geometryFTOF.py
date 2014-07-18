
import random
import math
from Particle import Particle


dataProvider = DataBaseLoader.getTimeOfFlightConstants()
print dataProvider.toString()

ftofDetector   = FTOFDetectorFactory.createDetector(dataProvider)
ftofDetector.show()


