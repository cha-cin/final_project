import paho.mqtt.client as mqtt
import os
def on_connect(client, userdata, flags, rc):
    client.subscribe("One")
    client.subscribe("Two")
    client.subscribe("Three")
    client.subscribe("Four")
    client.subscribe("Five")
    client.subscribe("Six")
    client.subscribe("Seven")
    client.subscribe("Eight")
    client.subscribe("Nine")
    client.subscribe("Ten")
    client.subscribe("Eleven")
    client.subscribe("Twelve")
 



def on_message(client, userdata, msg):
    topic_select=0
    if msg.topic == 'One':
        print('YEE_1')
        topic_select=0
    if msg.topic == 'Two':
        print('YEE_2')
        topic_select=1
    if msg.topic == 'Three':
        print('YEE_3')
        topic_select=2
    if msg.topic == 'Four':
        print('YEE_4')
        topic_select=3
    if msg.topic == 'Five':
        print('YEE_5')
        topic_select=4
    if msg.topic == 'Six':
        print('YEE_6')
        topic_select=5
    if msg.topic == 'Seven':
        print('YEE_7')
        topic_select=6
    if msg.topic == 'Eight':
        print('YEE_8')
        topic_select=7
    if msg.topic == 'Nine':
        print('YEE_9')
        topic_select=8
    if msg.topic == 'Ten':
        print('YEE_10')
        topic_select=9
    if msg.topic == 'Eleven':
        print('YEE_11')
        topic_select=10
    if msg.topic == 'Twelve':
        print('YEE_12')
        topic_select=11

    #print(msg.topic+" "+str(msg.payload))
    want=str(msg.payload)[2:(len(str(msg.payload))-1)]
    str2 = ''
    i=0

    while i < len(want):
        str2 = str2+want[i]
        i=i+1
    print(str2)

    f = open('sensor_status.txt', 'r+')
    f.seek(topic_select,0)
    f.write(str2)
    #print(bytes.decode(want))
    f.close()

    #os.system('python3 homeassistant_nodemcu_publish.py')

f = open('sensor_status.txt', 'w')
f.write("000000000000000000000000")
f.close()

f = open('direction.txt', 'w')
f.write("000000000000000000000000")
f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.2.200", 1883, 60)
client.loop_forever()
