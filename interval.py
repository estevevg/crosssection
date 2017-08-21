import sys
import crosssection
import json

inputFile1 = sys.argv[1]
inputFile2 = sys.argv[2]
i1 = int(sys.argv[3])
i2 = int(sys.argv[4])

data1 = crosssection.readFile(inputFile1)
data2 = crosssection.readFile(inputFile2)

shift = crosssection.crossSectionInterval(data1, data2, i1, i2)
print json.dumps(shift)
dout = crosssection.applyShiftToData(data2, shift['shift'])

crosssection.saveData(dout, inputFile2)

crosssection.printPlot(data1, dout)
#crosssection.printData(data1)
