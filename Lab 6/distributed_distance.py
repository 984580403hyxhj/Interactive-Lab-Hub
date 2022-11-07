import time
import qwiic
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/your/topic/here'
ToF = qwiic.QwiicVL53L1X()


while True:
    try:
        ToF.start_ranging()  # Write configuration bytes to initiate measurement
        time.sleep(.005)
        distance = ToF.get_distance()  # Get the result of the measurement from the sensor
        time.sleep(.005)
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0
        s = "Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet)
        print(s)
        client.publish(topic, s)

    except Exception as e:
        print(e)
    time.sleep(0.25)