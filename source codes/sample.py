import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='root',passwd='sql123',database='electronics')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
c1.execute("select Product_no,Product_name from elect")
data=c1.fetchall()
print("PRODUCT NUMBER\t|PRODUCT NAME")
for i in data:
    print(i[0],i[1],sep="\t\t|")
