
#Read Data from MQTT server and write into a CSV file 
import csv 
import paho.mqtt.client as mqtt
import time

header = ['LED2','LED3','LED4','LED5','LED6','LED7','LED8','LED9','LED10','LED11','LED12']

def on_connect(client, userdata, flags, rc):
    print("Connected ")
    client.subscribe("Stud Location")

#studtest = [['LED2 - ON'],['LED4 - OFF']]

def on_msg(client, userdata, message):
    #print(str(message.payload.decode("utf-8")))
    temp = (message.payload.decode("utf-8"))
    stud = temp.split(',')
    print(stud)
    with open('stud.csv', 'a', newline='') as file: # w to write, a to append existing csv file 
        writer = csv.writer(file, delimiter =",")
        writer.writerow(stud)

   
mqttServer = "wallinsiders.fenteale.com"
client = mqtt.Client()
client.on_connect = on_connect
with open('stud.csv', 'w', newline='') as file: # w to write, a to append existing csv file 
    writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
    writer.writerow(header)
    
client.on_message = on_msg
client.connect(mqttServer)
   


client.loop_forever() 
