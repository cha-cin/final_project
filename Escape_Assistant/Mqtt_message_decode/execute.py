import machine
D0=machine.Pin(0, machine.Pin.OUT)
D4=machine.Pin(4, machine.Pin.OUT)
D5=machine.Pin(5, machine.Pin.OUT)
D2=machine.Pin(2,machine.Pin.OUT)
def open():
	def a():
		D0.low()
		D4.low()
		D5.low()
		D2.high()
	def b():
		D0.high()
		D4.low()
		D5.low()
		D2.high()
	def c():
		D0.low()
		D4.high()
		D5.low()
		D2.high()
	def d():
		D0.high()
		D4.high()
		D5.low()
		D2.high()
	def e():
		D0.low()
		D4.low()
		D5.high()
		D2.high()
	def f():
		D0.high()
		D4.low()
		D5.high()
		D2.high()
	def g():
		D0.low()
		D4.high()
		D5.high()
		D2.high()
	def h():
		D0.high()
		D4.high()
		D5.high()
		D2.high()
	def i():
		D0.high()
		D4.high()
		D5.high()
		D2.low()
	def j():
		D0.low()
		D4.high()
		D5.high()
		D2.low()

