import random
import timex
import time

def getDataCO2():
    co2 = random.randint(0,1000)
    print(co2)
    return co2

def writeCO2():
    f = open("dataco2", "a")
    a = str(getDataCO2())
    b = ","
    c = str(timex.getTime())
    f.write(a+b+c+'\n')
    f.close

def resetCO2data():
    file = open("dataco2", "r+")
    file.truncate(0)
    file.close()
    time.sleep(1)

def loopDataCo2():
    file = open("dataco2", "r+")
    file.truncate(0)
    file.close()
    while True:
        writeCO2()
        time.sleep(1)


def getDataTMP():
    tmp = random.randint(0,1000)
    print(tmp)
    return tmp

def writeTMP():
    f = open("datatemperatur", "a")
    a = str(getDataCO2())
    b = ","
    c = str(timex.getTime())
    f.write(a+b+c+'\n')
    f.close

def resetTMPdata():
    file = open("datatemperatur", "r+")
    file.truncate(0)
    file.close()
    time.sleep(1)

def loopDataTMP():
    file = open("datatemperatur", "r+")
    file.truncate(0)
    file.close()
    while True:
        writeTMP()
        time.sleep(1)

def getDataPAR():
    tmp = random.randint(0,1000)
    print(tmp)
    return tmp

def writePAR():
    f = open("datapar", "a")
    a = str(getDataCO2())
    b = ","
    c = str(timex.getTime())
    f.write(a+b+c+'\n')
    f.close

def resetPARdata():
    file = open("datapar", "r+")
    file.truncate(0)
    file.close()
    time.sleep(1)

def loopDataPAR():
    file = open("datapar", "r+")
    file.truncate(0)
    file.close()
    while True:
        writePAR()
        time.sleep(1)