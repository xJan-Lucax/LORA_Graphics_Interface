import data_converter
import time
import threading

def thread_function(name):

file = open("dataco2","r+")
file.truncate(0)
file.close()

while True:
    data_converter.writeCO2()
    time.sleep(1)