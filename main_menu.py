import admission
import student_data
import more
import report
import mysql.connector as co
def main_menu():
  while True:
    #main_menu.clrscreen()
    print("\t\t-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("\n\t\t*****Welcome To School Management System*****")
    print("\n\t\t.............................................")
    print("\n\t\t    ***** Gita Vidya Mandir School *****")
    print("1: Admission")
    print("2: Student Data")
    print("3: Graphical Report")
    print("4: ...For More Details")
    print("5: Exit")
    print("\n\t\t-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    choice=int(input("\nEnter Your Choice:-"))
    if choice==1:
      admission.ADM_MENU()
    elif choice==2:
      student_data.STU_MENU()
    elif choice==3:
      report.gr_rep()
    elif choice==4:
      more.more_data()
    elif choice==5:
      break
    else:
      print("Error: Invalid Choice Try Again.....")
      conti=input("Press Any Key To Continue:-")
