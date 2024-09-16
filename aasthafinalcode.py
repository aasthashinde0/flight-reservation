import mysql.connector

mycon=mysql.connector.connect(host="localhost",username="root",passwd="1234",database="flightreservation")

if mycon.is_connected() == False :
    print("Not connected ")

cursor=mycon.cursor()    

    
def maintainflightschedule():
    while True :
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO TICKET SCHEDULE ")
        print("\t"*3,"*"*73,"\n","\n")
        print("1. ADD NEW SCHEDULE")
        print("2. MODIFY FLIGHT SCHEDULE ")
        print("3. DELETE FLIGHT SCHEDULE ")
        print("0. RETURN TO MAIN MENU ")
        ch='4'
        ch=input("ENTER YOUR CHOICE :")
        if ch == '1':
            ADDNEWSCHEDULE()
        elif ch=='2':
            MODIFYFLIGHTSCHEDULE()
        elif ch=='3':
            DELETEFLIGHTSCHEDULE()
        elif ch=='0':
            break
        else :
            print("Invalid choice")


def ADDNEWSCHEDULE():
    print("\t"*3,"*"*73)
    print("\t"*5,"ADD NEW SCHEDULE ")
    print("\t"*3,"*"*73,"\n","\n")
    
    FLIGHT_DATE=input(" ENTER FLIGHT DATE : ")
    FLIGHT_TIME=input(" ENTER FLIGHT TIME: ")
    CITY_FROM=input(" ENTER CITY FROM: ")
    CITY_TO=input(" ENTER CITY TO: ")
    FARE=input(" ENTER FARE: ")
    cursor.execute("select * from aircraft")
    dt=cursor.fetchall()
    for row in dt:
        print(row)
    AIRCRAFT_N0=int(input(" ENTER AIRCRAFT NO: "))

    qr="insert into flight_schedule1 (FLIGHT_DATE, FLIGHT_TIME, CITY_FROM, CITY_TO, AIRCRAFT_NO,FARE) values ('%s','%s','%s','%s',%s,%s)"%(FLIGHT_DATE, FLIGHT_TIME,CITY_FROM,CITY_TO,AIRCRAFT_N0,FARE)

    cursor.execute(qr)

    mycon.commit()
    

def MODIFYFLIGHTSCHEDULE():
   while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO MODIFY FLIGHT SCHEDULE ")
        print("\t"*3,"*"*73,"\n","\n")
        cursor.execute("select * from flight_schedule1 ")
        dt=cursor.fetchall()
        for row in dt:
            print(row)

        FLIGHT_SCH_ID=int(input("ENTER FLIGHT SCHEDULE ID: "))
        qr="select * from flight_schedule1 where flight_sch_id=%s"%(FLIGHT_SCH_ID)
        print("qr is ",qr)
        cursor.execute(qr)
        dt=cursor.fetchall()

        for row in dt:
           FLIGHT_DATE =row[1]
           FLIGHT_TIME=row[2]
           CITY_FROM=row[3]
           CITY_TO=row[4]
           AIRCRAFT_NO=row[5]

        print(" "*3,"1.FLIGHT DATE: ")
        print(" "*3,"2.FLIGHT TIME:")
        print(" "*3,"3.CITY FROM: ")
        print(" "*3,"4.CITY TO: ")
        print(" "*3,"5.AIRCRAFT NO: ")

        
        ch=int(input(" "))

        while True:
            if ch ==1:
                FLIGHT_DATE=input("ENTER FLIGHT DATE : ")
                break
            elif ch==2:
                FLIGHT_TIME=input("ENTER FLIGHT TIME : ")
                break
            elif ch==3:
                CITY_FROM=input("ENTER CITY FROM: ")
                break
            elif ch==4:
                CITY_TO=input("ENTER CITY TO : ")
                break
            elif ch==5:
                AIRCRAFT_NO=input("ENTER  AIRCRAFT NO : ")
                break
                
            else :
                 print("Invalid Choice ")
                 break

        qr="update flight_schedule1 set FLIGHT_DATE ='%s',FLIGHT_TIME='%s',CITY_FROM='%s', City_to='%s' where FLIGHT_SCH_ID=%s "%(FLIGHT_DATE,FLIGHT_TIME,CITY_FROM,CITY_TO,FLIGHT_SCH_ID)
      

        cursor.execute(qr)

        mycon.commit()
        break
       

    
def DELETEFLIGHTSCHEDULE():
    while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO DELETE FLIGHT DETAILS ")
        print("\t"*3,"*"*73,"\n","\n")
        cursor.execute("select * from flight_schedule1")
        dt=cursor.fetchall()
        for row in dt:
            print(row)
        FLIGHT_SCH_ID=int(input("ENTER FLIGHT SCH ID : "))
        qr="DELETE from aircraft where AIRCRAFT_NO=%s"%(FLIGHT_SCH_ID)
        val=(FLIGHT_SCH_ID)
        cursor.execute(qr,val)
        mycon.commit()
        break


def maintainflightdetails():
    while True :
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO TICKET SCHEDULE ")
        print("\t"*3,"*"*73,"\n","\n")
        print("1. ADD NEW FLIGHT")
        print("2. MODIFY FLIGHT DETAILS")
        print("3. DELETE FLIGHT  ")
        print("0. RETURN TO MAIN MENU ")
        ch='4'
        ch=input("ENTER YOUR CHOICE :")
        if ch == '1':
            ADDNEWFLIGHT()
        elif ch=='2':
            MODIFYFLIGHTDETAILS()
        elif ch=='3':
            DELETEFLIGHT()
        elif ch=='0':
            break
        else :
            print("Invalid choice ")

def ADDNEWFLIGHT():
    print("\t"*3,"*"*73)
    print("\t"*5,"ADD NEW FLIGHT")
    print("\t"*3,"*"*73,"\n","\n")
    
    airname=input("Aircraft Name : ")
    airtype=input("Aircraft Type : ")
    tseats=int(input("Aircraft Total Seats : "))

    qr="insert into aircraft (Aircraft_name,Aircraft_type,total_seats) values ('%s','%s',%s)"%(airname,airtype,tseats)


    cursor.execute(qr)

    mycon.commit()


def MODIFYFLIGHTDETAILS():
    while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO MODIFY FLIGHT DETAILS ")
        print("\t"*3,"*"*73,"\n","\n")
        cursor.execute("select * from aircraft")
        dt=cursor.fetchall()
        for row in dt:
            print(row)

        AIRCRAFT_NO=int(input("ENTER AIRCRAFT NO: "))
        qr="select * from aircraft where AIRCRAFT_NO=%s"%(AIRCRAFT_NO)
        cursor.execute(qr)
        dt=cursor.fetchall()

        for row in dt:
            AIRCRAFT_NAME=row[1]
            AIRCRAFT_TYPE=row[2]
            TOTAL_SEATS=row[3]

        print(" "*3,"1.AIRCRAFT NAME ")
        print(" "*3,"2.AIRCRAFT TYPE ")
        print(" "*3,"3.TOTAL SEATS ")
        ch=int(input("ENTER A CHOICE "))

        while True:
            if ch ==1:
                 AIRCRAFT_NAME=input("ENTER AIRCRAFT NAME: ")
                 break
            elif ch==2:
                 AIRCRAFT_TYPE=input("ENTER AIRCRAFT TYPE: ")
                 
                 break
            elif ch==3:
                 TOTAL_SEATS=input("ENTER TOTAL SEATS: ")
                 
                 break
            else :
                 print("Invalid Choice ")
                 break

        qr="update  aircraft set AIRCRAFT_NAME='%s',AIRCRAFT_TYPE='%s',TOTAL_SEATS='%s' where AIRCRAFT_NO=%s "%(AIRCRAFT_NAME,AIRCRAFT_TYPE,TOTAL_SEATS,AIRCRAFT_NO)


        cursor.execute(qr)

        mycon.commit()
        break
       
    


def DELETEFLIGHT():
    while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO DELETE FLIGHT DETAILS ")
        print("\t"*3,"*"*73,"\n","\n")
        cursor.execute("select * from aircraft")
        dt=cursor.fetchall()
        for row in dt:
            print(row)
        AIRCRAFT_NO=int(input("ENTER AIRCRAFT NO: "))
        qr="DELETE from aircraft where AIRCRAFT_NO=%s"%(AIRCRAFT_NO)
        val=(AIRCRAFT_NO)
        cursor.execute(qr,val)
        mycon.commit()
        break


def passangerdetails():
    while True :
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO PASSENGER MMAINTANCE ")
        print("\t"*3,"*"*73,"\n","\n")
        print("1. ADD NEW PASSENGER")
        print("2. MODIFY PASSENGER DETAILS")
        print("3. DELETE PASSENGER  ")
        print("0. RETURN TO MAIN MENU ")
        ch='4'
        ch=input("ENTER YOUR CHOICE :")
        if ch == '1':
            ADDNEWPASSENGER()
        elif ch=='2':
            MODIFYPASSENGER()
        elif ch=='3':
            DELETEPASSANGER()
        elif ch=='0':
            break
        else :
            print("Invalid choice ")

def ADDNEWPASSENGER():
    print("\t"*3,"*"*73)
    print("\t"*5,"ADD NEW FLIGHT")
    print("\t"*3,"*"*73,"\n","\n")
    
    
    PNR_NAME=input("PNR NAME: ")
    BIRTH_DATE=input("BIRTH DATE : ")
    ID_PROOF=input("ID PROOF : ")
    PNR_MOBILE=input("MOBILE NO : ")
    PNR_EMAIL=input("EMAIL  : ")

    qr="insert into passenger ( PNR_NAME, BIRTH_DATE, ID_PROOF, PNR_MOBILE, PNR_EMAIL) values ('%s','%s','%s','%s','%s')"%( PNR_NAME, BIRTH_DATE, ID_PROOF, PNR_MOBILE, PNR_EMAIL)


    cursor.execute(qr)

    mycon.commit()
    
            
def MODIFYPASSENGER():
    while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO MODIFY PASSANGER DETAILS ")
        print("\t"*3,"*"*73,"\n","\n")
        cursor.execute("select * from passenger")
        dt=cursor.fetchall()
        for row in dt:
            print(row)

        PNR_NO=int(input("ENTER PNR NO: "))
        qr="select * from passenger where PNR_NO=%s"%(PNR_NO)
        cursor.execute(qr)
        dt=cursor.fetchall()

        for row in dt:
            PNR_NAME=row[1]
            BIRTH_DATE=row[2]
            ID_PROOF=row[3]
            PNR_MOBILE=row[4]
            PNR_EMAIL=row[5]

        print(" "*3,"1.PNR NAME: ")
        print(" "*3,"2.BIRTH DATE:")
        print(" "*3,"3.ID PROOF: ")
        print(" "*3,"4.:PNR MOBILE ")
        print(" "*3,"5.PNR EMAIL: ")

        
        ch=int(input("ENTER A CHOICE "))

        while True:
            if ch ==1:
                PNR_NAME =input("ENTER PNR NAME: ")
                break
            elif ch==2:
                BIRTH_DATE=input("ENTER BIRTH_DATE: ")                 
                break
                 
            elif ch==3:
                ID_PROOF=input("ENTER  ID_PROOF: ")
                break

            elif ch==4:
                PNR_MOBILE =input("ENTER  PNR_MOBILE : ")
                break
                
            elif ch==5:
                PNR_EMAIL =input("ENTER PNR EMAIL : ")
                break

            else :
                print("Invalid Choice ")
                break

        qr="update  passenger set PNR_NAME='%s',BIRTH_DATE='%s',ID_PROOF='%s',PNR_MOBILE='%s',PNR_EMAIL='%s' where PNR_NO=%s "%( PNR_NAME, BIRTH_DATE, ID_PROOF, PNR_MOBILE, PNR_EMAIL,PNR_NO)


        cursor.execute(qr)

        mycon.commit()
        break

def DELETEPASSANGER():
    while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO DELETE PASSANGER DETAILS ")
        print("\t"*3,"*"*73,"\n","\n")
        cursor.execute("select * from passenger")
        dt=cursor.fetchall()
        for row in dt:
            print(row)
        PNR_NO=int(input("ENTER PNR NO: "))
        qr="DELETE from passenger where PNR_NO=%s"%(PNR_NO)
        val=(PNR_NO)
        cursor.execute(qr,val)
        mycon.commit()
        break
       


def maintainticketdetails():
    while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO TICKET DETAILS ")
        print("\t"*3,"*"*73,"\n","\n")
        print("1. ISSUE TICKETS ")
        print("2.CANCEL TICKET")
        print("0. RETURN TO MAIN MENU ")
        ch='4'
        ch=input("ENTER YOUR CHOICE :")
        if ch == '1':
            ISSUETICKETS()
        elif ch=='2':
            CANCELTICKET()
        elif ch=='0':
            break
        else :
            print("Invalid Choice ")

def ISSUETICKETS():
    
  
    print("\t"*3,"*"*73)
    print("\t"*5,"WELCOME TO  ISSUE TICKETS ")
    print("\t"*3,"*"*73,"\n","\n")
    cursor.execute("select * from passenger ")
    dt=cursor.fetchall()
    for row in dt:
            print(row)

    PNR_NO=int(input("ENTER PNR NO: "))
    qr="select * from flight_schedule1 "
    cursor.execute(qr)
    dt=cursor.fetchall()

    for row in dt:
          print(row)

    flight_sch_id=int(input("Enter flight schedule id "))
 
        
    seat_no=int(input("ENTER seat no "))

        
    qr="insert into tickets (seat_no,pnr_no,flight_sch_id) values (%s,%s,%s)"%(seat_no, PNR_NO, flight_sch_id)


    cursor.execute(qr)

    mycon.commit()
                



         
def CANCELTICKET():
    print("\t"*3,"*"*73)
    print("\t"*5,"CANCEL TICKET ")
    print("\t"*3,"*"*73,"\n","\n")

   
    cursor.execute("select * from tickets ")
    dt=cursor.fetchall()
    for row in dt:
            print(row)

    ticket_no =int(input("Enter ticket no to be cancelled "))

    qr="update tickets set can_status='Yes' where ticket_no=%s"%(ticket_no)

    cursor.execute(qr)

    mycon.commit()


   

    

def reports():
      while True:
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO REPORTS ")
        print("\t"*3,"*"*73,"\n","\n")
        print("1. DAILY COLLECTION REPORT ")
        print("2. CITY WISE TOTAL TICKETS REPORT ")
        print("0. RETURN TO MAIN MENU ")
        ch='4'
        ch=input("ENTER YOUR CHOICE :")
        if ch == '1':
            qr="SELECT SUM(FARE), FLIGHT_DATE FROM TICKETS T, flight_schedule1 F WHERE T.FLIGHT_SCH_ID=F.FLIGHT_SCH_ID GROUP BY FLIGHT_DATE "
            cursor.execute(qr)

            data=cursor.fetchall()
            print("Date                  Total Fare ")
            for row in data:
                print(row[1],"          ",row[0])
                
        elif ch=='2':
            qr="select  city_to, count(ticket_no) from tickets t, flight_schedule1 f where t.flight_sch_id=f.FLIGHT_SCH_ID group by  city_to"


            cursor.execute(qr)

            data=cursor.fetchall()
            print("Total Tickets        City ")
            for row in data:
                print("     ",row[1],"             ",row[0])
        elif ch=='0':
            break
        else :
            print("Invalid Choice ")
    
def final():
    while True :
        print("\t"*3,"*"*73)
        print("\t"*5,"WELCOME TO AIRWAY MANAGEMENT PROGRAM")
        print("\t"*3,"*"*73,"\n","\n")
        print("1. MAINAIN FLIGHT SCHEDULE")
        print("2. MAINAIN FLIGHT DETAILS")
        print("3. MAINTAIN TICKET DETAILS")
        print("4.PASSANGER DETAILS ")
        print("5. Reports DETAILS ")        
        print("0. EXIT")
        ch='5'
        ch=input("ENTER YOUR CHOICE :")
        if ch == '1':
            maintainflightschedule()
        elif ch=='2':
           maintainflightdetails()
        elif ch=='3':
            maintainticketdetails()
        elif ch=='4':
            passangerdetails()
        elif ch=='5':
            reports()
        elif ch=='0':
            break
        else:
            print("INVALID CHOICE")
final()
