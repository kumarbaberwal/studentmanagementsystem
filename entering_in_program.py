import new_user
import old_user
while True:
  
  print("\t\t-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
  print("\n\t\t*****Welcome To School Management System*****")
  print("\n\t\t.............................................")
  print("\n\t\t    ***** Gita Vidya Mandir School *****")
  print("1: Old User")
  print("2: New User")
  print("3: Exit")
  print("\n\t\t-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
  choice=int(input("\nEnter Your Choice:- "))
  if choice==1:
    old_user.gun()
  elif choice==2:
    new_user.fun()
  elif choice==3:
    break
  else:
    print("Error: Invalvid Choice Try Again.....")
    conti=input("Press Any Key To Continue:-")




    
  



