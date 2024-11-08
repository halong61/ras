import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.IN)

try:
    while True:
        btn = gpio.input(21)
        print(btn)
except KeyboardInterrupt:
        gpio.cleanup()