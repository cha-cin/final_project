from umqtt.simple import MQTTClient 
import ubinascii
import machine
import micropython
import time
import decode
import execute
import sys


def do_connect():
    import network

    SSID = 'Master'
    PASSWORD = 'rty91119'

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Network configuration:', sta_if.ifconfig())



# Default MQTT server to connect to
SERVER = "192.168.2.200"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"thirteen"
TOPIC_Publish = b"One"
TOPIC_Publish2 = b"Rat"
PORT_NO = 1883     #change to mqtt port no.
USERNAME = "pi"
PASSWORD = "raspberry"


state = 0

def sub_cb(topic, msg):
    global state
    #print((topic, msg))
    #msg is bytes
    msg_decode=str(msg,'utf-8')
    print(msg_decode)
    #print(type(msg_decode))
    decode.de(msg_decode)

def main(server=SERVER):
    #c = MQTTClient (CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
    # Subscribed messages will be delivered to this callback
    #c.set_callback(sub_cb)
    #c.connect()
    #c.subscribe(TOPIC)
    #print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    #change=1
    #try:
    while 1:
        c = MQTTClient (CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
        # Subscribed messages will be delivered to this callback
        c.set_callback(sub_cb)
        c.connect()
        c.subscribe(TOPIC)
        print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
        change=1
        #micropython.mem_info()
        led =machine.Pin(9, machine.Pin.IN)
        led2 =machine.Pin(12, machine.Pin.IN)
        if led.value() is 0:
            c.publish(TOPIC_Publish,'1')
            print("SD2 ok!")
        if led2.value() is 0:
            c.publish(TOPIC_Publish2,'1')
            print("D6 ok!")
        c.wait_msg()
        del sys.modules['execute']
        import execute
        execute.open()
        f = open('execute.py', 'r')
        sss = f.read()
        print(sss)
        f.close()
        print("finish")
        c.disconnect()
            #time.sleep(1)
            #machine.reset()
#鼠：Rat，牛：Ox，虎：Tiger，兔：Hare，龙：Dragon ，蛇：Snake，马：Horse，羊：Sheep，猴：Monkey，鸡：Cock，狗：Dog，猪：Boar           

    #finally:
        #print("finish!!!")
        #time.sleep(1)
        #machine.reset()

    #c.disconnect()

    
    #c.disconnect()
if __name__ == '__main__':
#    load_config()
#    setup_pins()
    do_connect()
    main()