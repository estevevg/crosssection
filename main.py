import sys
import crosssection
import json

inputFile1 = sys.argv[1]
inputFile2 = sys.argv[2]
th = float(sys.argv[3])
#i2 = sys.argv[4]

data1 = crosssection.readFile(inputFile1)
data2 = crosssection.readFile(inputFile2)

dout = crosssection.crossSection(data1, data2, th)
print json.dumps(dout)

crosssection.printPlot(data2)
#crosssection.printData(data1)
