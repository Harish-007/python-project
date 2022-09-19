import mysql.connector

travels=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kali@123",
    database="travels_db"
)
print("*"*20)
print("welcome to Explore 360 travel agency")
print("*"*20)
def menu():
    print("To know about our services press 1")
    print("To know the basic Tour service press 2 ")
    print("To know about our budget tour service press 3")
    print("To know about about VIP tour services press 4")
    print("To avail travel guide services press 5")
    print("if you have no idea press 6")
    print("If you are ready with your destination,travel mode and ready to explore press 7")

def services():
    print("we provide a travel tour packages with exiting offers")
    print("we provide travel guide services for your travel")
    print("we provide three levels of tour packages like basic,budget and VIP")

def guide():
    print("**********///This is a special service for our customers///**********")
    print("lets cut out the chase, here you can add travel guide to your package or avail personally")
    if tour_package == "vip":
        print("You are lucky you'll be provided with a travel guide for free")
    elif tour_package == "budget":
        print("You'll need to pay extra 3000 for a travel guide")
    elif tour_package=="basic":
        print("we hope there'll be no need for a travel guide but still if you want you need to pay extra 4000 rupees")
    else:
        print("if you are availing personally you need to pay 7000 rupess along with foox expenses of travel guide")

def basic_tour():
         mycursor=travels.cursor()
         mycursor.execute("create table if not exists basic(places varchar(100), budget int, days int) ")
         print("All set lets view the basic packages")
         sql = "insert into basic(places,budget,days) values(%s,%s,%s)"
         val = [ ("kodaikanal",4000,3),
                 ("kolli hills",4000,3),
                 ("meghamalai",4000,3),
                 ("valparai",3000,3)
               ]            
         mycursor.executemany(sql,val)
         travels.commit()
         mycursor.execute("select DISTINCT* from basic")
         result=mycursor.fetchall()
         for i in result:
            print(i)

def Vip_tour():
    print("*"*19)
    print("You are wise to opt this one coz this is our premium package")
    print("*"*19)
    mycursor=travels.cursor()
    mycursor.execute("create table if not exists Vip (Places varchar(100),budget int, total_days int)")
    sql=("insert into Vip(places,budget,total_days) values(%s,%s,%s)")
    val = [
            ("Goa",15000,10),
            ("Manali",13000,11),
            ("Ladakh",25000,14),
            ("Himalayas",30000,15),
            ("Maldieves",20000,10),
            ("Andaman and Nicobar",30000,14)
          ]
    mycursor.executemany(sql,val)
    travels.commit()
    mycursor.execute("select DISTINCT* from Vip")
    results=mycursor.fetchall()
    for i in results:
        print(i) 

def budget_tour():
    mycursor=travels.cursor()
    mycursor.execute("create tabe if not exists budget(places varchar(100),budget int ,total_days int)")
    print("All set lets view")
    sql="insert into budget(places,budget,total_days)values(%s,%s,%s)"
    val=[
          ("mumbai",8000,5),
          ("banglore",9000,5),
          ("ooty",7000,5),
          ("Mysore",7000,5)
        ]
    mycursor.executemany(sql,val)
    travels.commit()
    mycursor.execute("select Distinct* from budget")
    results=mycursor.fetchall()
    for i in results:
        print(i)

def choice():
    if budget<=4000 and days<=3:
        basic_tour()
    elif budget<=9000 and days<=5:
        budget_tour()
    elif budget<=30000 and days<=15:
        Vip_tour()

def registration(name,age,tour_date,tour_package,guide):
    mycursor=travels.cursor()
    mycursor.execute("create table if not exists tour(name varchar(100),age int,tour_date int,tour_package varchar(100),guide varchar(100))")
    print("ok lets enter the datas")
    sql="insert into tour(name,age,tour_date,tour_package,guide)values(%s,%d,%d,%s,%s)"
    val=("name,age,tour_date,tour_package,guide")
    mycursor.execute(sql,val)
    travels.commit()
    mycursor.execute("select DISTINCT*from tour")
    results=mycursor.fetchall()
    for i in results:
        print(i)

user=int(input("Enter your number : "))
if user ==1:
    services()
if user==2:
    basic_tour()
if user==3:
    budget_tour()
if user==4:
    Vip_tour()
if user==5:
    tour_package=input("Enter the tour package you opt fot : ").lower().strip()
    guide()
if user==6:
    budget=input("Please enter your budget :")
    days = input("please enter the number of days you wanter to travel :")
    choice()
if user==8:
    decision=input("have you made your choice:").lower().strip()
    if decision=="yes":
        name=input("Enter your name : ").lower().strip()
        age=int(input("Enter your age : "))
        tour_date=input("Enter your tour date : ").lower().strip()        
        tour_package=input("enter your tour package : ").lower().strip() 
        registration(name,age,tour_date,tour_package,guide) 
    else:
        wish=input("do you dont want to make a tour with travel :").lower().strip()
        if wish=="yes":
            print("we felt that you would join a tour with us ok if you change your mind please contact us")
            rating=int(input("please give us any rating from 1 to 5 : "))
            review=input("dou you find something useful with travel 360 : ").lower().strip()
            if rating>3 and review=="yes":
                print("thankyou please visit us again")
            else:
                needs=[]
                improve=input("what improvement we need to do to satisfy your need :")
                needs.append(improve)
if user>8:
    print("there is only numbers from 1 to 8")


     