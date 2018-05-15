# coding:utf-8
import pymysql

db = pymysql.connect(host="192.168.5.126", user="root", passwd="Nc.123456", db="folders", port=3306, charset="utf8")
cursor = db.cursor()
for i in range(1, 888):
    cursor.execute('''insert into test02_num2count(number) values(''' + "%s" % i + ''')''')
db.commit()
db.close()