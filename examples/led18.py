import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

def ledon():
    gpio.output(18,1);
def ledoff():
    gpio.output(18,0);
    
def cleanup():
    gpio.cleanup()