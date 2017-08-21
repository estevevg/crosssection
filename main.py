# -*- coding: utf-8 -*-
import sys
import crosssection
import json

inputFile1 = sys.argv[1]
inputFile2 = sys.argv[2]
th = float(sys.argv[3])
#i2 = sys.argv[4]

data1 = crosssection.readFile(inputFile1)
data2 = crosssection.readFile(inputFile2)

shift = crosssection.crossSection(data1, data2, th)
print json.dumps(shift)
dout = crosssection.applyShiftToData(data2, shift['shift'])

crosssection.saveData(dout, inputFile2)

crosssection.printPlot(data1, dout)
#crosssection.printData(data1)
