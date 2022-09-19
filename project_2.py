import mysql.connector
Atm=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kali@123",
    database="Atm_db"
)
mycursor=Atm.cursor()
mycursor.execute("create table if not exists atm(customer_Id int primary key auto_increment,name varchar(100),Bank_balance int,password int)")
print("Hii...")
print("*"*25)
print("Welcome to trust bank")
print("*"*25)
print("please insert your ATM card to continue")
ATM=input("Have you inserted your atm card :").lower().strip()
Next = input("To get into menu please enter continue :").lower().strip()
if ATM=="yes" and Next=="continue":
    print("To register a new account press 0")
    print("To check balance info press 1")
    print("for Withdrawal press 2 ")
    print("To check your account information press 4")
    print("To deposit cash press 5")
    print("To change pin press 6")
    print("For more services press 7")
else:
    print("please insert your atm card to continue with us")
def register(n,b,p):
    mycursor=Atm.cursor()
    sql="Insert into atm (name,Bank_balance,password) values (%s,%s,%s)"
    val=(n,b,p)
    mycursor.execute(sql,val)
    Atm.commit()
    print("Registration successfull and initial payment of 1000 should be deposited")

def balance():
    mycursor=Atm.cursor()
    mycursor.execute("select*from atm where name='%s'"%(name)) 
    row=mycursor.fetchone() 
    if mycursor.rowcount==1:
        mycursor.execute("select*from where password='%s'"%(password))   
        row=mycursor.fetchone()
        if mycursor.rowcount==1:
            for i in row:
                print(i)
        else:
            print("the pin you entered is invalid please check with your bank ")
    else:
        print("No such name is registered")
def Withdrawal():
    mycursor=Atm.cursor()
    mycursor.execute("select Bank_balance from atm where password='%s'"%(password))
    bal=mycursor.fetchone()
    results=list(bal)
    for i in results:
        get=(int(i))
        total=get-a
    mycursor.execute("update atm set Bank_balance='%s' where password='%s'"%(total,password)) 
    print("Your balance is :",total)

user=int(input("please enter the number for service :"))
if user==0:
    n=input("please enter your name :")
    b=1000
    p=int(input("Please enter your password in 4 digit numerics :"))
    register(n,b,p)
if user==1:
     password=int(input("please enter your pin :"))
     balance()
if user==2:
    password=int(input("please enter your pin :"))
    a=int(input("enter the amount you want to withdraw :"))
    Withdrawal()