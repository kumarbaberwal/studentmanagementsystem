import student_data
import mysql.connector as co
mycon=co.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1")
cursor=mycon.cursor()
cursor.execute("create database if not exists GVM")
cursor.execute("use GVM")
cursor.execute("create table if not exists student_data  (Academic_Session varchar(20),Student_Name varchar(20),Admission_No varchar(10),Clas varchar(10),Roll_No int(10),Sub1 varchar(10),Sub2 varchar(10),Sub3 varchar(10))")
def STU_MENU():
  while True:
    #student_data.clrScreen()
    print("\n\t\t.............................................")
    print("\n\t\t*****Welcome To School Management System*****")
    print("\n\t\t.............................................")
    print("\n\t\t        ***** Student Data Menu *****")
    print("1: Add Student Record")
    print("2: Show Student Details")
    print("3: Search Student Details")
    print("4: Delete Student Records")
    print("5: Edit Student Records")
    print("6: Exit")
    print("\n\t\t.............................................")
    choice=int(input("\nEnter Your Choice :- "))
    if choice==1:
      student_data.Add_Records()
    elif choice==2:
      student_data.Show_Stu_Details()
    elif choice==3:
      student_data.Search_Stu_Details()
    elif choice==4:
      student_data.Delete_Stu_Details()
    elif choice==5:
      student_data.Edit_Stu_Details()
    elif choice==6:
      return
    else:
      print("Error: Invalid Choice Try Again.....")
      conti="Press Any Key To Return To Main Menu :-"
    

def Add_Records():
  try:
    mycon=co.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
    cursor=mycon.cursor()
    session=input("Enter Academic Session (eg;2020-2021) : ")
    name=input("Enter Student Name : ")
    adno=input("Enter Admission Number : ")    
    clas=input("Enter Class : ")
    rno=input("Enter Roll Number : ")
    sub1=input("Enter First Subject : ")
    sub2=input("Enter Second Subject : ")
    sub3=input("Enter Third Subject : ")

    Query="insert into student_data(Academic_Session,Student_Name,\
Admission_No,Clas,Roll_No,Sub1,Sub2,Sub3) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(session,name,adno,clas,rno,sub1,sub2,sub3)
    cursor.execute(Query,val)
    mycon.commit()
    print("Record Has Been saved In Student Data Table")
  except:
    print("Error")
    
def Show_Stu_Details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  import pandas as pd
  row=pd.read_sql("Select * From student_data",mycon)
  print(row)

def Search_Stu_Details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  ac=input("Enter Admission Number :- ")
  st="select * from student_data where Admission_No='%s'"%(ac)
  import pandas as pd
  data=pd.read_sql(st,mycon)
  print(data)

def Delete_Stu_Details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  st="delete from student_data where Admission_No='%s'"%(ac)
  cursor.execute(st)
  mycon.commit()
  print("Data Deleted Successfully")

def Edit_Stu_Details():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()


  print("1: Edit Academic Session : ")
  print("2: Edit Student Name : ")
  print("3: Edit Class : ")
  print("4: Edit Roll Number : ")
  print("5: Edit First Subject : ")
  print("6: Edit Second Subject : ")
  print("7: Edit Third Subject : ")
  print("8: Exit")
  print("\n\t\t-----------------------------------------------")
  choice=int(input("\nEnter Your Choice :- "))
  if choice==1:
    student_data.edit_Academic_Session()
  elif choice==2:
    student_data.edit_Student_Name()
  elif choice==3:
    student_data.edit_clas()
  elif choice==4:
    student_data.edit_Roll_No()
  elif choice==5:
    student_data.edit_Sub1()
  elif choice==6:
    student_data.edit_Sub2()
  elif choice==7:
    student_data.edit_Sub3()
  elif choice==8:
    return
  else:
    print("Error: Invalid Choice Try Again.....")
    conti="Press Any Key To Return To"
def edit_Academic_Session():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Academic Session :- ")
  bc="update student_data set Academic_Session=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updated")
def edit_Student_Name():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Student Name :- ")
  bc="update student_data set Student_Name=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
def edit_clas():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Class :- ")
  bc="update student_data set clas=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
def edit_Roll_No():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Roll Number :- ")
  bc="update student_data set Roll_No=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
def edit_Sub1():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct First Subject :- ")
  bc="update student_data set Sub1=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
def edit_Sub2():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Second Subject :- ")
  bc="update student_data set Sub2=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
def edit_Sub3():
  mycon.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  ac=input("Enter Admission Number :- ")
  ca=input("Enter Correct Third Subject :- ")
  bc="update student_data set Sub3=%s where Admission_No=%s"
  upd=(ca,ac)
  cursor.execute(bc,upd)
  mycon.commit()
  print("Data Successfully Updates")
  
