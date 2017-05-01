from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython


def do_connect():
    import network

    SSID = 'Mster'
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

    
def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
    # Subscribed messages will be delivered to this callback
    
    c.connect()
    c.publish(TOPIC,'hello fire1')
    print("Connected to %s, publish to %s topic" % (server, TOPIC))

    
    c.disconnect()

if __name__ == '__main__':
#    load_config()
#    setup_pins()
    do_connect()
    main()