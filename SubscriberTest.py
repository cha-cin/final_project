import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("123")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.2.102", 1883, 60)
client.loop_forever()

# Publisher.py
#import paho.mqtt.client as mqtt
 
#_g_cst_ToMQTTTopicServerIP = "192.168.2.150"
#_g_cst_ToMQTTTopicServerPort = 1883 #port
#_g_cst_MQTTTopicName = "123" #TOPIC name
 
#mqttc = mqtt.Client("python_pub")
#mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)
#mqttc.publish(_g_cst_MQTTTopicName, "Hello")