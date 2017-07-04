import machine
import time
led =machine.Pin(4, machine.Pin.OUT)
def open():
    led.high()
    #time.sleep(5)
    #led.low()


def lof():
    led.low()
open()