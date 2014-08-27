from LundReader import LundReader
import sys

file = sys.argv[1]

reader = LundReader(file)

fileOut = open('lund_output.data','w')

for i in range(0,800):
    reader.readEvent()
    print '----> Reading event',i
    if(reader.getPidCount(321)==1 and reader.getPidCount(-321)==1 and reader.getPidCount(22)==0):
        event = reader.getEvent()
        for line in event:
            print line,
            fileOut.write(line)
