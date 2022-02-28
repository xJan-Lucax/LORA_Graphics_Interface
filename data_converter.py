import random
import timex
import time

def getDataCO2():
    co2 = random.randint(0,10)
    print(co2)
    return co2

def writeCO2():
    f = open("dataco2", "a")
    a = str(getDataCO2())
    b = ","
    c = str(timex.getTime())
    f.write(a+b+c+'\n')
    f.close

def loopData():
    file = open("dataco2", "r+")
    file.truncate(0)
    file.close()

    while True:
        writeCO2()
        time.sleep(1)