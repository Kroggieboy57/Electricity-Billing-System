import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='root',passwd='sql123',database='electronics')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
c1.execute("select Product_no from elect")
data=c1.fetchall()
print(data)
leng=len(data)
print(leng)
buy=list(data)
print(buy)
en=input("enter the product number")
print(en)
eng=('('+en+','+')')
print(eng)
for i in range(leng):
    print(data[i])
    print(eng)
    if data[i]==eng:
       print("print product number exits")
       break
    else:
        print("product number not exits")

    
