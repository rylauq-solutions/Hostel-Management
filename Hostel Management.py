'''Suppose the Database named HOSTEL MANAGEMENT and Table named HOSTEL are already created as follows:
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor=con.cursor()
mycursor.execute("Create Database HOSTEL_MANAGEMENT")
mycursor.execute("create table HOSTEL(rgn_no int primary key,name varchar(20),address varchar(100),room_no int,dept varchar(15),fees int,bal int);")'''

import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="HOSTEL_MANAGEMENT")
if (con.is_connected()==False):
    print('Connection Failed, TRY AGAIN...')
else:
    cur=con.cursor()
    print("                                   WELCOME TO  HOSTEL MANAGEMENT                                   ")
    def Again():
        Auto=True
        while Auto==True:
            print("MAKE YOUR PREFERENCE:")
            print("     1.ADMISSION FORM")
            print("     2.STATUS CHECKING")
            print("     3.UPDATE DETAILS")
            print("     4.AUTHORITIES")
            print("     5.EXIT")
            print()
            choice=int(input('ENTER YOUR CHOICE:'))
            print()

            def AdmnForm():
                rgn=int(input("ENTER YOUR REGISTRATION NUMBER:"))
                name=input("ENTER YOUR NAME:")
                add=input("ENTER YOUR ADDRESS:")
                room_no=int(input("ENTER YOUR ROOM NUMBER:"))
                dept=input("ENTER YOUR DEPARTMENT:")
                fees=int(input("ENTER YOUR FEES:"))
                bal=int(input("ENTER YOUR BALANCE:"))
                query1="insert into HOSTEL value({},'{}','{}',{},'{}',{},{});".format(rgn,name,add,room_no,dept,fees,bal)
                cur.execute(query1)

            def StatusCheck():
                ch=int(input('Enter Your Department:'))
                print()
                if ch==1:
                    show="Select * from HOSTEL where dept like 'COMPUTER%' or dept like 'Computer%' or dept like 'computer%';"
                    cur.execute(show)
                elif ch==2:
                    show="Select * from HOSTEL where dept='ENGLISH' or dept='English' or dept='english';"
                    cur.execute(show)
                elif ch==3:
                    show="Select * from HOSTEL where dept='PHYSICS' or dept='Physics' or dept='physics';"
                    cur.execute(show)
                elif ch==4:
                    show="Select * from HOSTEL where dept='CHEMISTRY' or dept='Chemistry' or dept='chemistry';"
                    cur.execute(show)
                elif ch==5:
                    show="Select * from HOSTEL where dept='MATHS' or dept='Maths' or dept='maths';"
                    cur.execute(show)
                else:
                    print("~~~It is Advised to RECHECK the ENTRIES~~~")
                    
            def UpdateDetails(ch,r):
                if ch==1:
                    n_name=input("ENTER YOUR NAME (~updated):")
                    cur.execute("Update HOSTEL set name='{}' where rgn_no={};".format(n_name,r))
                    print('~~~UPDATION SUCCESSFULL~~~')
                elif ch==2:
                    n_add=input("ENTER YOUR ADDRESS (~updated):")
                    cur.execute("Update HOSTEL set address='{}' where rgn_no={};".format(n_add,r))
                    print('~~~UPDATION SUCCESSFULL~~~')
                elif ch==3:
                    n_room_no=int(input("ENTER YOUR ROOM NUMBER (~updated):"))
                    cur.execute("Update HOSTEL set room_no={} where rgn_no={};".format(room_no,r))
                    print('~~~UPDATION SUCCESSFULL~~~')
                elif ch==4:
                    n_dept=input("ENTER YOUR DEPARTMENT (~updated):") 
                    cur.execute("Update HOSTEL set dept='{}' where rgn_no={};".format(n_dept,r))
                    print('~~~UPDATION SUCCESSFULL~~~')
                elif ch==5:
                    n_fees=int(input("ENTER YOUR FEES (~updated):"))
                    cur.execute('Update HOSTEL set fees={} where rgn_no={};'.format(n_fees,r))
                    print('~~~UPDATION SUCCESSFULL~~~')
                elif ch==6:
                    n_bal=int(input("ENTER YOUR BALANCE (~updated):"))
                    cur.execute('Update HOSTEL set bal={} where rgn_no={};'.format(n_bal,r))
                    print('UPDATION SUCCESSFULL')
                else:
                    print("~~~INVALID CHOICE~~~")

            if choice==1:
                AdmnForm()
                con.commit()
                print()
                print()

            elif choice==2:
                print("DEPARTMENT PREFERENCE:")
                print(" 1. Computer Science")
                print(" 2. English")
                print(" 3. Physics")
                print(" 4. Chemistry")
                print(" 5. Maths")
                print()
                StatusCheck()
                details=cur.fetchall()
                if details==[]:
                    print("~~~No Record Found~~~")
                    print()
                else:
                    l=len(details)
                    for x in range(0,l):
                        print("Registration Number:",details[x][0])
                        print("Name:",details[x][1])
                        print("Address:",details[x][2])           
                        print("Room Number:",details[x][3])
                        print("Department:",details[x][4])
                        print("Fees:",details[x][5])           
                        print("Balance:",details[x][6])
                        print()

            elif choice==3:
                print("What Do You Wish To Update?")
                print(" 1. Name")
                print(" 2. Address")
                print(" 3. Room Number")
                print(" 4. DEPARTMENT")
                print(" 5. Fees")
                print(" 6. Balance")
                print()
                r=int(input("ENTER YOUR REGISTRATION NUMBER:"))
                print()
                ch=int(input('Enter What You Wish To Update:'))
                print()
                UpdateDetails(ch,r)
                con.commit()
                print()
                print()

            elif choice==4:
                input("ENTER PASSWORD:")
                print("~~~Incorrect Password, TRY AGAIN...~~~")
                print()
                print()

            elif choice==5:
                Auto=False

            else:
                print('~~~INVALID CHOICE~~~')
                print()

    try:
        Again()

    except:
        print()
        print()
        print("~~~~~Unwanted Error Occured:(~~~~~")
        print()
        print()
        Again()

    finally:
        print('~~~~~Over & Out,HAVE A NICE DAY:)~~~~~')
