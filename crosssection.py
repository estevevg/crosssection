import json
import numpy as np
import matplotlib.pyplot as plt

MIN_SHIFT = -300
MAX_SHIFT = 300

def readFile(fname):
    data = json.loads('{"canal": [],"read": []}')
    with open(fname, "r") as lines:
        for l in lines:
            print l
            data["canal"].append(int(l.split("\t")[0]))
            data["read"].append(float(l.split("\t")[1].split("\r")[0]))
    return data

def printData(data):
    i = 0
    for c in data["canal"]:
        print str(c)+"  "+str(data["read"][i])
        i+=1

def crossSection(d1, d2, i1, i2):
    while(i1 < i2):
        d1["read"][i1] = d1["read"][i1] - d2["read"][i1]
        i1 += 1
    return d1

def crossSection2(d1, d2):
    shift = MIN_SHIFT
    sol = {}
    while shift < MAX_SHIFT:
        r = applyShift(d1, d2, shift)
        sol = compareShift(shift, t, sol)
        shift += 1
    return s

def applyShift(d1, d2, shift):
    i = 0
    out = 0
    for r in d1["read"]:
        outp += r - d2["read"][i] + shift
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
