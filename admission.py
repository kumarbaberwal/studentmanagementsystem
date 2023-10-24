import admission
import warnings
warnings.filterwarnings("ignore")
import mysql.connector as co
mycon=co.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1")
cursor=mycon.cursor()
cursor.execute("create database if not exists GVM")
cursor.execute("use GVM")
cursor.execute("create table if not exists  admission (adno varchar(10),rno int(10),Sname varchar(15),address varchar(20),phon varchar(225),clas varchar(5))")
def ADM_MENU():
  while True:
    #admission.clrScreen()
    print("\t\t...............................................")
    print("\n\t\t*****Welcome To School Management System*****")
    print("\n\t\t.............................................")
    print("\n\t\t              *****Admission*****")
    print("1: Admission Details")
    print("2: Show Admission Details")
    print("3: Search")
    print("4: Deletion Of Records")
    print("5: Update Admission Details")
    print("6: Return")
    print("\n\t\t_____________________________________________")
    choice=int(input("\nEnter Your Choice :- "))
    if choice==1:
      admission.admin_details()
    elif choice==2:
      admission.show_admin_details()
    elif choice==3:
      admission.search_admin_details()
    elif choice==4:
      admission.delete_admin_details()
    elif choice==5:
      admission.edit_admin_details()
    elif choice==6:
      return
    else:
      print("Error: Invalid Choice Try Again.....")
      conti="Press Any Key To Return To Main Menu :-"
def admin_details():
  try:
    import mysql.connector as co
    mycon=co.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
    cursor=mycon.cursor()
    adno=input("Enter Admission Number : ")
    rno=int(input("Enter Roll No. : "))
    Sname=input("Enter Student Name : ")
    address=input("Enter Address : ")
    phon=input("Enter Phone Number : ")
    clas=input("Enter Class : ")

    Query="insert into admission(adno,rno,sname,address,phon,clas) values(%s,%s,%s,%s,%s,%s)"
    val=(adno,rno,Sname,address,phon,clas)
    cursor.execute(Query,val)
    mycon.commit()
    print("Record Has Been saved In Admission Table")
  except:
    print("Error")

def show_admin_details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  b="Select * From admission"
  import pandas as pd
  a=pd.read_sql(b,mycon)
  print(a)
def search_admin_details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  st="select * from admission where adno='%s'"%(ac)
  import pandas as pd
  a=pd.read_sql(st,mycon)
  print(a)
def delete_admin_details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  st="delete from admission where adno='%s'"%(ac)
  cursor.execute(st)
  mycon.commit()
  print("Data Deleted Successfully")
def edit_admin_details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()


  print("1: Edit Name : ")
  print("2: Edit Addresss : ")
  print("3: Phone Number : ")
  print("4: Return : ")
  print("\n\t\t-----------------------------------------------")
  choice=int(input("\nEnter Your Choice :- "))
  if choice==1:
    admission.edit_name()
  elif choice==2:
    admission.edit_address()
  elif choice==3:
    admission.edit_phon()
  elif choice==4:
    return
  else:
    print("Error: Invalid Choice Try Again.....")
    conti="Press Any Key To Return To"
def edit_name():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Student Name :- ")
  bc="update admission set Sname=%s where adno=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updated")
def edit_address():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Student Address :- ")
  bc="update admission set address=%s where adno=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
def edit_phon():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Phone Number :- ")
  bc="update admission set phon=%s where adno=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updated")



  
  
  
    
