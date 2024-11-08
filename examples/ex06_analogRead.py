import spidevRead as sr
import time
import led18

try:
    while True:
        data = sr.analog_read(0)
        #data의 값을 확인하여
        #밝아지면 꺼지고, 어두워지면 켜지는 led코드 작성하기
        if(data<800):
            print(data)
            led18.ledon()
            time.sleep(1)
        else:
            print(data)
            led18.ledoff()
            time.sleep(1)
except KeyboardInterrupt:
    led18.cleanup 
        
