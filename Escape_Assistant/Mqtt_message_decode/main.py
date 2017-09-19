from umqtt.simple import MQTTClient 
import ubinascii
import machine
import micropython
import time
import execute
import decode



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
    c = MQTTClient (CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
    execute.open()
    change=1
    try:
        while 1:
            #micropython.mem_info()
            led =machine.Pin(9, machine.Pin.IN)
            led2 =machine.Pin(12, machine.Pin.IN)
            if led.value() is 0 and led2.value() is 1:
                c.publish(TOPIC_Publish,'10')
                print("ok!")
            elif led.value() is 0 and led2.value() is 0:
                c.publish(TOPIC_Publish,'11')
                print("ok!")
            elif led.value() is 1 and led2.value() is 0:
                c.publish(TOPIC_Publish,'01')
            elif led.value() is 0:
                if led2.value() is 0:
                    c.publish(TOPIC_Publish,'11')
                    print("ok!")
            elif led2.value() is 0:
                if led.value() is 0:
                    c.publish(TOPIC_Publish,'11')
                    print("ok!")
            c.wait_msg()
            print("finish!!!")
            time.sleep(1)
            machine.reset()
            

    finally:
        print("finish!!!")
        time.sleep(1)
        machine.reset()

    c.disconnect()

    
    #c.disconnect()
if __name__ == '__main__':
#    load_config()
#    setup_pins()
    do_connect()
    main()