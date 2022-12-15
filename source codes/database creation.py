import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='sql123')
c1=conn.cursor()
c1.execute("create database electronics")
print("data base created")
