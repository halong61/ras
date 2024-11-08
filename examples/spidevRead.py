import spidev

spi = spidev.SpiDev() #spi 객체를 생성
spi.open(0,0) #spi 통신을 시작
spi.max_speed_hz = 1000000 #통신 속
 
def analog_read(portChanner):
    adc = spi.xfer2([1, (8+portChanner)<<4, 0])
    data = ((adc[1]&3)<<8)+adc[2]
    return data