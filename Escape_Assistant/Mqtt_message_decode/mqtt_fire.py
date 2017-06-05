from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
def publish_fire():
	SERVER = "192.168.2.200"
	CLIENT_ID = ubinascii.hexlify(machine.unique_id())
	PORT_NO = 1883     #change to mqtt port no.
	USERNAME = "pi"
	PASSWORD = "raspberry"
	server=SERVER
	c = MQTTClient(CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
	# Subscribed messages will be delivered to this callback
	TOPIC1 = b"fire1"
	TOPIC2 = b"fire2"
	c.connect()
	c.publish(TOPIC1,'hello fire1')
	c.publish(TOPIC2,'hello fire2')
	print("mqtt_publish finish!!")