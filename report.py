import report
import student_data
import mysql.connector as co
def gr_rep():
  while True:
    #student_data.clrScreen()
    print("\n\t\t.............................................")
    print("\n\t\t*****Welcome To School Management System*****")
    print("\n\t\t.............................................")
    print("\n\t\t        ***** Graphical Report *****")
    print("1: Class Wise Student Details")
    print("2: Session Wise Student Details")
    print("3: Exit")
    print("\n\t\t.............................................")
    choice=int(input("\nEnter Your Choice :- "))
    if choice==1:
      report.cwsr()
    elif choice==2:
      report.swsr()
    elif choice==3:
      return
    else:
      print("Error: Invalvid Choice Try Again.....")
      conti="Press Any Key To Return To Main Menu: "
def cwsr():
  mycon=co.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  cursor.execute("select distinct(clas) from student_data")
  data=cursor.fetchall()
  clas=[]
  for row in data:
    clas.append(row)
  print("Distinct Classes : ",clas)
  cursor.execute("select count(clas) from student_data group by clas")
  data=cursor.fetchall()
  no_o_s=[]
  for row in data:
    no_o_s.append(row)
  print("Student Present : ",no_o_s)
  import matplotlib.pyplot as pl
  import numpy as np
  arr=np.array(no_o_s)
  flat_array=arr.flatten()
  print(pl.pie(flat_array,labels=clas,autopct="%1.1f%%"))
  pl.show()

def swsr():
  mycon=co.connect(host='localhost',user='root',password='Kumar',port=3306,charset="latin1",database='GVM')
  cursor=mycon.cursor()
  cursor.execute("select distinct(Academic_Session) from student_data")
  data=cursor.fetchall()
  clas=[]
  for row in data:
    clas.append(row)
  print("Distinct Sessions: ",clas)
  cursor.execute("select count(Academic_Session) from student_data group by Academic_Session")
  data=cursor.fetchall()
  no_o_s=[]
  for row in data:
    no_o_s.append(row)
  print("Student Present : ",no_o_s)
  import matplotlib.pyplot as pl
  import numpy as np
  arr=np.array(no_o_s)
  a=arr.flatten()
  print(pl.pie(a,labels=clas,autopct="%1.1f%%"))
  pl.show()
  
    
