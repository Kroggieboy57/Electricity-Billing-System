import mysql.connector as sql
import datetime
conn=sql.connect(host='localhost',user='root',passwd='sql123',database='electronics')
#if conn.is_connected():
 # print("Successfully Connected")
c1=conn.cursor()
t_date=datetime.date.today()
t_time=datetime.datetime.now()
print("DATE:",t_date.day,"/",t_date.month,"/",t_date.year,"TIME:",t_time.hour ,":",t_time.minute     )
print("Welcome To SSA Electronics Shop Management System")
print("1.Purchase Items")
print("2.Stock")
print("3.Exit")
choice=int(input("Enter the Choice - "))
if choice==1:
    import sample
    v_product_no=int(input("\nEnter the Product Number : "))
    if v_product_no==('123456')or('623455')or('645124')or('645224')or('647123')or('647124')or('698655'):
        c1.execute("select Product_name,Stock,Price_per from elect where Product_no="+str(v_product_no))
        data=c1.fetchall()
        for row in data:
            print("Available Stock Details ".center(30," "))
            print(f"Product name: {row[0]}".center(30," "))
            print(f"Stock: {row[1]}".center(30," "))
            print("Price per product Rs:",row[2])
            conn.commit()
            print("\nDo you want to buy this item:")
            print("1.Yes")
            print("2.No")
            ch=int(input("Enter the Choice - "))
            if ch==1:
                q=int(input("enter how much do you need="))
                g=int(row[2])*q
                print("The amount is Rs:",g)
                print("Do you want to continue:")
                print("1.Yes")
                print("2.No")
                cho=int(input("Enter the Choice - "))
                if cho==1:
                    c1.execute("update elect set Stock=Stock- "+ str(q) + " where Product_no="+str(v_product_no))
                    print(" Items purchased successfully")
                    conn.commit()
                    print("Do you want to buy any more:")
                    print("1.Yes")
                    print("2.No")
                    dad=int(input("Enter the choice:"))
                    if dad==1:
                        import purchase
                    elif dad==2:
                        print("Thank you")
                        print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                        print("================================================================================")
                    else:
                        print("Invalid choice")
                        print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                        print("==============================================================================")
                        
                elif cho==2:
                    print("Thank you")
                    print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                    print("================================================================================")
                else:
                    print("ERROR 404:DTETCTED")
            elif ch==2:
                print("Thank you")
                print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                print("==============================================================================")
            else:
                print("Invalid choice")
                print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
                print("==============================================================================")
    else:
        print("Invalid choice of product number")
        print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
        print("==============================================================================")
elif choice==2:
    print("1.Add stock")
    print("2.View stock")
    print("3.Update new stock")
    chi=int(input("Enter the Choice - "))
    if chi==1:
       v='vijay'
       c=input("Enter the password:")
       if c==v:
           import sample
           a=int(input("Enter the Product Number : "))
           b=int(input("Enter how much stock must be updated:"))
           c1.execute("update elect set Stock = Stock + "+str( b ) + " where Product_no = " +str(a))
           conn.commit()
           c1.execute("select Product_name,Product_no,Stock from elect where Product_no="+str(a))
           dat=c1.fetchall()
           for row in dat:
               print("Available Stock Details ")
               print("Product name:",row[0])
               print("Product number:",row[1])
               print("Stock:",row[2])
               print("Updated succesfully")
       else:
           print ("Password is wrong")
    elif chi==2:
        import sample
        z=int(input("Enter the Product Number : "))
        c1.execute("select Product_name,Product_no,Stock,Price_per from elect where Product_no="+str(z))
        dat=c1.fetchall()
        for row in dat:
               print("Available Stock Details ")
               print("Product name:",row[0])
               print("Product number:",row[1])
               print("Stock:",row[2])
               print("Price per product Rs:",row[3])
        print("Do you want to continue:")
        print("1.Yes")
        print("2.No")
        chg=int(input("Enter the Choice - "))
        if chg==1:
            import buy
            
        else:
            print("Thank you")
            print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
            print("=======================================================================")
    elif chi==3:
        de='krog'
        da=input("Enter the password:")
        if de==da:
            print("welcome to ssa electronic shop")
            fi=int(input("enter the new product number(in 6 digits):"))
            fe=input("enter the new product name:")
            st=int(input("enter the stock to be updated:"))
            price=int(input("enter the price per product:"))
            c1.execute("insert into elect values('{}',{},'{}','{}')".format(fe,fi,st,price))
            print("updated successfully")
            conn.commit()
        else:
             print("Incorrect Password, ACCESS DENIED!")
    else:
        print("invalid choice")
elif choice==3:
    print("Thank you")
    print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
    print("=============================================================================")
else :
    print("INVALID CHOICE OF OPTION")
    print("Any kind of bulk or small orders of elctronic items contact SSA electronics shop")
    print("=============================================================================")
