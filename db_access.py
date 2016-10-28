# coding: UTF-8

import mysql.connector

import key

conn = mysql.connector.connect(user='root', password=key.DB, host='localhost', database='test')
cur = conn.cursor()

cur.execute("select * from user;")

for row in cur.fetchall():
    print (row[0], row[1])

cur.close
conn.close

