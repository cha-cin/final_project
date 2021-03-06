from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import time


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
TOPIC = b"fire1"
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
    
    str2 = ''
    i=0
    while i < len(msg_decode):
        if msg_decode[i] is '\\':
            if msg_decode[i+1] is 'n':
                str2 = str2+'\n'
                i=i+2
            elif msg_decode[i+1] is 't':
                str2 = str2+'\t'
                i=i+2
            else:
                i=i+1
        else:
            str2 = str2+msg_decode[i]
            i=i+1
    
    print(str2)
    f = open('main.py', 'w')
    f.write(str2)
    f.close()

def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    
    while(True):
        try:
            while 1:
                #micropython.mem_info()
                c.wait_msg()
                
        finally:
            print("finish!!!")
            time.sleep(2)
            machine.reset()
            
    c.disconnect()
    
	
    #c.disconnect()
if __name__ == '__main__':
#    load_config()
#    setup_pins()
    do_connect()
    main()