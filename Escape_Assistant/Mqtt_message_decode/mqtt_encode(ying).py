import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    for i in range(3):
    #print("Connected with result code "+str(rc))
    #client.subscribe("fire1")
    #client.subscribe("fire2")
    #client.subscribe("fire3")
        client.subscribe("fire"+str(i))
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    want=str(msg.payload)[2:(len(str(msg.payload))-1)]
    str2 = ''
    i=0
    #print(want)
    print(len(want))
    print('\n\n\n')
    #if(len(want)==24):

    while i < len(want):
        if want[i] is '\\':
            if want[i+1] is 'n':
                str2 = str2+'\n'
                i=i+2
            elif want[i+1] is 't':
                str2 = str2+'\t'
                i=i+2
            else:
                i=i+1
        else:
            str2 = str2+want[i]
            i=i+1
    print(str2)
        
    
    #want[i] = want[i]+'\t'
    #print(want)
    
    #print(str2.decode('utf-8'))
    f = open('new_excute.py', 'w')
    f.write(str2)
    #print(bytes.decode(want))
    f.close()



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.2.200", 1883, 60)
client.loop_forever()