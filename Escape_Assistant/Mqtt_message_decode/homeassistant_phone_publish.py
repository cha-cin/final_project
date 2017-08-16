import paho.mqtt.client as mqtt

f = open("direction.txt", 'r')
c_str = f.read()
f.close()

_g_cst_ToMQTTTopicServerIP = "192.168.2.200"
_g_cst_ToMQTTTopicServerPort = 1883 #port
_g_cst_MQTTTopicName = "test" #TOPIC name

mqttc = mqtt.Client("python_pub")
mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)
mqttc.publish(_g_cst_MQTTTopicName,c_str)
print(_g_cst_MQTTTopicName)


print (c_str)
