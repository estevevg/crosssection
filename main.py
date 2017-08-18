import sys
import crosssection
import json

inputFile1 = sys.argv[1]
inputFile2 = sys.argv[2]
i1 = sys.argv[3]
i2 = sys.argv[4]

data1 = crosssection.readFile(inputFile1)
data2 = crosssection.readFile(inputFile2)

dout = crosssection.crossSection(data1, data2, i1, i2)

crosssection.printData(data)
