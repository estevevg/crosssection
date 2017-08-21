import json
import numpy as np
import matplotlib.pyplot as plt

MIN_SHIFT = -300
MAX_SHIFT = 300

def readFile(fname):
    data = json.loads('{"canal": [],"read": []}')
    with open(fname, "r") as lines:
        for l in lines:
            #print l
            data["canal"].append(int(l.split("\t")[0]))
            data["read"].append(float(l.split("\t")[1].split("\r")[0]))
    return data

def printData(data):
    i = 0
    for c in data["canal"]:
        print str(c)+"  "+str(data["read"][i])
        i+=1

def printPlot(data):
    plt.plot(data['read'])
    plt.ylabel('Reads')
    plt.xlabel('Channels')
    plt.show()

def crossSection(d1, d2, th):
    shift = MIN_SHIFT
    sol = {}
    while shift < MAX_SHIFT:
        r = applyShift(d1, d2, shift, th)
        sol = compareShift(shift, r, sol)
        shift += 1
    return sol

def applyShift(d1, d2, shift, th):
    i = 0
    outp = 0
    for r in d1["read"]:
        if r < th:
            outp += r - d2["read"][i] + shift
        else:
            print r
        i += 1
    return outp

def compareShift(shift, res, sol):
    if "out" not in sol:
        sol["shift"] = shift
        sol["out"] = res
        return sol
    if abs(res) < abs(sol["out"]):
        sol["shift"] = shift
        sol["out"] = res
        return sol
    return sol

def crossSectionInterval(d1, d2, i1, i2):
    shift = MIN_SHIFT
    sol = {}
    while shift < MAX_SHIFT:
        r = applyShiftInterval(d1, d2, shift, i1, i2)
        sol = compareShift(shift, r, sol)
        shift += 1
    return sol

def applyShiftInterval(d1, d2, shift, i1, i2):
    i = 0
    outp = 0
    for r in d1["read"]:
        if i < i1 or i > i2:
            outp += r - d2["read"][i] + shift
        i += 1
    return outp
