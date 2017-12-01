#!/usr/local/bin/python
#encoding:utf-8

import MySQLdb

conn = MySQLdb.connect(
    host = '192.168.8.239',
    port = 3306,
    user = 'root',
    passwd = 'danxiaowei2008',
    db = 'test'
)

cur = conn.cursor()

#cur.execute("create table student(id int,name varchar(200),class varchar(30),age varchar(10))")

cur.execute("insert into student values(1,'Dxw','3 year class',9)")

sqli = "insert into student values(%s,%s,%s,%s)"
cur.execute(sqli,(2,'Hulu','2 year 1 class','7'))

sqli = "insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[
    (3,'Ab','1 year 1 class','6'),
    (3,'DD','2 year 1 class','7'),
    (3,'Ds','2 year 2 class','8')
    ])

print cur.execute("update student set class='3 year 2 class' where name = 'DD' ")

print cur.execute("delete from student where age = '8' ")

total = cur.execute("select * from student")
info = cur.fetchmany(total)
for ii in info:
    print ii

cur.close()
conn.commit()
conn.close()