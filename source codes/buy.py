import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='root',passwd='sql123',database='electronics')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
t_date=datetime.date.today()
t_time=datetime.datetime.now()
print("DATE:",t_date.day,"/",t_date.month,"/",t_date.year,"TIME:",t_time.hour ,":",t_time.minute     )
print("Welcome To The Motherboard Electronics Shop Management System")
z=int(input("Enter the product number again:"))
c1.execute("select Product_name,Stock,Price_per from elect where Product_no="+str(z))
data=c1.fetchall()
for row in data:
    print("Available Stock Details ")
    print("Product name:",row[0])
    print("Stock:",row[1])
    print("Price per product Rs:",row[2])
    conn.commit()
    print("Do you want to buy this item:")
    print("1.Yes")
    print("2.No")
    ch=int(input("Enter the Choice - "))
    if ch==1:
        q=int(input("Enter Quantity - "))
        g=int(row[2])*q
        print("The amount is ₹",g)
        print("Do you want to continue:")
        print("1.Yes")
        print("2.No")
        cho=int(input("Enter the Choice - "))
        if cho==1:
            c1.execute("update elect set Stock=Stock- "+ str(q) + " where Product_no="+str(z))
            print(" Items purchased successfully")
            conn.commit()
            print(f"Date:{t_date.day}/{t_date.month}/{t_date.year}\tTIME: {t_time.hour}:{t_time.minute}")
            print("Invoice".center(50,"#"))
            print("Item\tQty\tPrice")
            print(f"Item\t{q}\t{g}")
            print(" Paid ".center(50,"-"))
        elif cho==2:
            print("Thank you")
            print("Any kind of bulk or small orders of elctronics contact The Motherboard electronics shop")
            print("================================================================================")
        else:
            print("ERROR 404:DETECTED")
    elif ch==2:
        print("Thank you")
        print("Any kind of bulk or small orders of elctronics contact The Motherboard electronics shop")
        print("==============================================================================")
    else:
        print("Invalid choice")
        print("Any kind of bulk or small orders of elctronics contact The Motherboard electronics shop")
        print("==============================================================================")
    
