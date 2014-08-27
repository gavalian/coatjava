from LundReader import LundReader
import sys

file = sys.argv[1]

reader = LundReader(file)

fileOut = open('lund_output.data','w')

icounter = 0
filtercounter = 0
while(reader.readEvent()):
    #print '----> Reading event',icounter
    icounter = icounter + 1
    if(reader.eventFilter([11,321,-321,2212])==True):
        #print '---> found event at record ',icounter
        filtercounter = filtercounter + 1
        event = reader.getEvent()
        for line in event:
            #print line,
            fileOut.write(line)


#-----------------------------------------------------
print '--> Events read = ',icounter,'  events filtered = ',filtercounter
