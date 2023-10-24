def fun():
  try:
    import pandas
    a=input("Enter New User Name :- ")
    b=input("Enter Your Password :- ")
    df1=pandas.DataFrame([[a,b]])
    df1.to_csv("C:\\Users\\HP\\Desktop\\Programming_Practices\\Student Management System\\user.csv",mode="a",header=False,index=False)
    print("Enter New User And Password Again")
    import old_user
    old_user.gun()
  except:
    
    import entering_in_program
