import ttn_storage_api
import time

def ttndatacheck():
    key = "NNSXS.KMD3MBZAVR4HCFMYJ3UTCVWZ34SVFRG3FAGGOWI.AWFTZON664S3GATFSI3COT7KAKKB42UK2D4QKIBOB3VXYYRU325A"
    r = ttn_storage_api.sensor_pull_storage("rfm95-sensor-data-atmega16", key, "100h")
    anzahlmessages = len(r)
    lastmessage = r[anzahlmessages-1]['result']['uplink_message']['decoded_payload']['bytes']
    zeitstempel = r[anzahlmessages-1]['result']['received_at']
    #print(zeitstempel)
    zeitstempelold = zeitstempel
    lastvalue = lastmessage[0]

    def writenewttndata(data, time):
        f = open("datattn", "a")
        a = str(data)
        b = ","
        c = str(time)
        f.write(a+b+c+'\n')
        f.close

    while True:
        r = ttn_storage_api.sensor_pull_storage("rfm95-sensor-data-atmega16", key, "100h")
        anzahlmessages = len(r)
        zeitstempel = r[anzahlmessages-1]['result']['received_at']
        #print(zeitstempel)

        if zeitstempel != zeitstempelold:
            lastmessage = r[anzahlmessages - 1]['result']['uplink_message']['decoded_payload']['bytes']
            lastvalue = lastmessage[0]
            zeitstempelold = zeitstempel
            zeitstempel = zeitstempel.replace("-", "")
            zeitstempel = zeitstempel.replace("T", "")
            zeitstempel = zeitstempel.replace(":", "")
            zeitstempel = zeitstempel.replace("Z", "")
            zeitstempel = zeitstempel.replace(".", "")
            zeitstempel = zeitstempel[0:14]
            int(zeitstempel)
            zeitstempel = int(zeitstempel) + int(10000)
            str(zeitstempel)
            print("Neuer Wert :",lastvalue, "Empfangen um :", zeitstempel)
            writenewttndata(lastvalue, zeitstempel)
            time.sleep(1)
        else:
            #print("Keine neuen Daten")
            time.sleep(1)
