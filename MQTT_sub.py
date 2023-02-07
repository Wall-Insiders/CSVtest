
# Test mqtt connection/sub on python
import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected ")
    client.subscribe("LED_TEST")


def on_msg(client, userdata, message):
    print(message.payload)

mqttServer = "wallinsiders.fenteale.com"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_msg
client.connect(mqttServer)
   

client.loop_forever() 

