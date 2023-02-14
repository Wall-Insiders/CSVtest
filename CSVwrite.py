
#Read Data from MQTT server and write into a CSV file 
import csv 
import paho.mqtt.client as mqtt
import time

header = ['LED2','LED3','LED4','LED5','LED6','LED7','LED8','LED9','LED10','LED11','LED12','POS_X','POS_Y']

def on_connect(client, userdata, flags, rc):
    print("Connected ")
    client.subscribe("stud_location")
    client.subscribe("position")

#studtest = [['LED2 - ON'],['LED4 - OFF']]
st_ready=False

def on_msg(client, userdata, message):
    print(message.topic, str(message.payload.decode("utf-8")))
    global sttemp
    global st_ready
    if message.topic == "stud_location":
        sttemp = (message.payload.decode("utf-8"))
        st_ready = True
    elif message.topic == "position" and st_ready == True and sttemp != None: 
        temp = (message.payload.decode("utf-8"))
        stud = sttemp.split(',')
        datapoint = stud.extend(temp.split(','))
        print("DP:", datapoint)
        with open('stud.csv', 'a', newline='') as file: # w to write, a to append existing csv file 
            writer = csv.writer(file, delimiter =",")
            writer.writerow(stud)
        st_ready = False

   
mqttServer = "wallinsiders.fenteale.com"
client = mqtt.Client()
client.on_connect = on_connect
with open('stud.csv', 'w', newline='') as file: # w to write, a to append existing csv file 
    writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
    writer.writerow(header)
    
client.on_message = on_msg
client.connect(mqttServer)
   


client.loop_forever() 
