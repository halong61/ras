import pymysql as ps
conn = ps.connect(host='localhost', user='root',passwd='1234', db='test')
curs = conn.cursor()
sql= 'select * from sensordb'
curs.execute(sql)
result = curs.fetchall()#execute의 결과물 전체를 받아오는 함수
print(result)
for sensing, ts in result:
    print('sensing:{} / timestamp:{}'.format(sensing,ts))