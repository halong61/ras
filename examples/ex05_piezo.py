import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

p = gpio.PWM(18,1) #PWM(핀번호, 주파수)
p.start(50) #chrl Dutycycle 설정
Fre = [262,294,330,349,392,440,493,523]

try:
    while True:
        for i  in Fre:
            p.ChangeFrequency(i)
            time.sleep(0.5)
        
except KeyboardInterrupt:
    gpio.cleanup()