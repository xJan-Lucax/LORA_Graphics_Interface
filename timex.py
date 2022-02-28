from datetime import datetime


def getTime():
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    print(current_time)
    return current_time

#while True:
#    print(getTime())
