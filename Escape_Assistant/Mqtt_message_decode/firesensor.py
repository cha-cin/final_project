import machine
led =machine.Pin(4, machine.Pin.IN)

def read():
    led.value()

