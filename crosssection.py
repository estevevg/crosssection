# -*- coding: utf-8 -*-
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

def saveData(data, name):
    file = open(str(name+"-shifted.dat"), "w+")
    i = 0
    for c in data["canal"]:
        file.write(str(c)+"  "+str(data["read"][i])+"\n")
        i+=1
    file.close()

def printPlot(d1, d2):

    plt.plot(d1['read'])
    plt.ylabel('Reads')
    plt.xlabel('Channels')

    plt.plot(d2['read'])
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

def applyShiftToData(data, shift):
    dout = json.loads('{"canal": [],"read": []}')
    i = 0
    for r in data['read']:
        dout['read'].append(r + shift)
        dout['canal'].append(data['canal'][i])
        i+=1
    return dout

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
