import more
import mysql.connector as co
def more_data():
      while True:
            #main_menu.clrscreen()
            print("\t\t-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            print("\n\t\t*****Welcome To School Management System*****")
            print("\n\t\t.............................................")
            print("\n\t\t    ***** Gita Vidya Mandir School *****")
            print("1: To Describe Admission Table")
            print("2: To Describe Student Table")
            print("3: Exit")
            print("\n\t\t-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            choice=int(input("\nEnter Your Choice:-"))
            if choice==1:
                  more.admission_table()
            elif choice==2:
                  more.student_table()
            elif choice==3:
                  break
            else:
                  print("Error: Invalvid Choice Try Again.....")
                  conti=input("Press Any Key To Continue:-")
def admission_table():
      import mysql.connector
      m=mysql.connector.connect(host="localhost",user="root",password="Kumar",port=3306,database="gvm",charset="latin1")
      cursor=m.cursor()
      import pandas
      a="describe admission"
      b=pandas.read_sql(a,m)
      print(b)
def student_table():
      import mysql.connector
      m=mysql.connector.connect(host="localhost",user="root",password="Kumar",port=3306,database="gvm",charset="latin1")
      cursor=m.cursor()
      import pandas
      a="describe student_data"
      b=pandas.read_sql(a,m)
      print(b)

