from trig import *

trig = TRIG("G9", "G8")

while True:
    pm10 = trig.getDust_pm10()
    if pm10 is not None:
        print ("DUST PM10 : {:<.2f}".format(pm10/1000))

    pm25 = trig.getDust_pm25()
    if pm25 is not None:
        print ("DUST PM2.5: {:<.2f}".format(pm25/1000))

    time.sleep_ms(500)
