def gun():
  import pandas
  df1=pandas.read_csv("C:\\Users\\HP\\Desktop\\Programming_Practices\\Student Management System\\user.csv",names=["User_Name","Password"])
  c=df1["User_Name"]
  d=df1["Password"]
  e=c.values.tolist()
  f=d.values.tolist()
  a=input("Enter User Name :- ")
  if a in e:
    b=input("Enter Password :- ")
    while True:
      if b in f:
        import main_menu
        main_menu.main_menu()
      else:
        print("Password Is In Correct")
        import entering_in_program
        break
  else :
    print("User Name Not Found")
    print("Create User And Password")
  
