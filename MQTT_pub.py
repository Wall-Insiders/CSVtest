
# Test mqtt connection/pub on python
import paho.mqtt.client as mqtt
import time
from random import randrange, uniform 

mqttServer = "wallinsiders.fenteale.com"
client = mqtt.Client("Stud_test")
client.connect(mqttServer)

while True:
    rNum = uniform(12.0, 28.0)
    client.publish("LED_TEST", rNum)
    print( float(rNum) )
    time.sleep(5)


 
