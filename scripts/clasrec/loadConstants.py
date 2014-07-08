from org.jlab.clas12.dbdata import DataBaseLoader

provider = DataBaseLoader.getCalorimeterConstants()
print provider.toString()

provider = DataBaseLoader.getTimeOfFlightConstants()
print provider.toString()
