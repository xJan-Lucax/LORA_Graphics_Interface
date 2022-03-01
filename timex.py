from datetime import datetime


def getTime():
    now = datetime.now()
    print(now)
    current_time = now.strftime("%Y%m%d%H%M%S")
    print(current_time)
    return current_time

#while True:
#    print(getTime())
