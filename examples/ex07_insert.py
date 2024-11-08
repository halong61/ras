import pymysql as ps
import spidevRead as sr
import time

conn = ps.connect(host='localhost', user='root',passwd='1234', db='test') #db연결을 정의

curs = conn.cursor() #db에서 작업을 대신 해주는 함수들이 포함
#exo6_analogRead 파일을 참고해서
#실제 조도센서의 값을 데이터 베이스에 넣어보기

for i in range(0,5):
    data = sr.analog_read(0)
    print(data)
    time.sleep(1)
    
    sql = f'insert into sensordb(sensing) values ({data})'
    curs.execute(sql)

conn. commit() #db의 데이터의 변화가 생겼으므로 커밋