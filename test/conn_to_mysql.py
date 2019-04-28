import pymysql
conn = pymysql.connect(host='172.20.10.11',port=3306, user='root', passwd='1qazXSW@', db='test')

concur = conn.cursor()

concur.execute('select * from youyuan')
print(concur.fetchall())