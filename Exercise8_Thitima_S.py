usernameinput = input("username:")
passwordinput = input("password:")
if usernameinput=="Thitima" and passwordinput=="122543":
 print("Welcome to Thitima Restaurant")
 print("What do you want to buy something?")
 print("This is all Menu in Thitima Restaurant")
 print("----------------------------")
 print("1.French fries  39 THB")
 print("2.Spaghetti     69 THB")
 print("3.Steak         59 THB")
 print("4.Fried chicken 49 THB")
 print("5.Noodle        30 THB")
 print("----------------------------")
 product=int(input("Do you want to buy?"))
    
 if    product==1:
  rates1=39
  print("Your product:",product," = ",rates1,"THB")
 elif  product==2:
  rates1=69
  print("Your product:",product," = ",rates1,"THB")
 elif  product==3:
  rates1=59
  print("Your product:",product," = ",rates1,"THB")
 elif  product==4:
  rates1=49
  print("Your product:",product," = ",rates1,"THB")
 elif  product==5:
  rates1=30
  print("Your product:",product," = ",rates1,"THB")
 number1=int(input("Do you want to number?"))
    
 if    product==1:
  rates1=39
  print("Total:",product," = ",rates1*number1,"THB")
 elif  product==2:
  rates1=69
  print("Total:",product," = ",rates1*number1,"THB")
 elif  product==3:
  rates1=59
  print("Total:",product," = ",rates1*number1,"THB")
 elif  product==4:
  rates1=49
  print("Total:",product," = ",rates1*number1,"THB")
 elif  product==5:
  rates1=30
  print("Total:",product," = ",rates1*number1,"THB")
 product=int(input("Do you want to buy?"))

 if    product==1:
  rates2=39
  print("Your product:",product," = ",rates2,"THB")
 elif  product==2:
  rates2=69
  print("Your product:",product," = ",rates2,"THB")
 elif  product==3:
  rates2=59
  print("Your product:",product," = ",rates2,"THB")
 elif  product==4:
  rates2=49
  print("Your product:",product," = ",rates2,"THB")
 elif  product==5:
  rates2=30
  print("Your product:",product," = ",rates2,"THB")
 number2=int(input("Do you want to number?"))
    
 if    product==1:
  rates2=39
  print("Total:",product," = ",rates2*number2,"THB")
 elif  product==2:
  rates2==69
  print("Total:",product," = ",rates2*number2,"THB")
 elif  product==3:
  rates2=59
  print("Total:",product," = ",rates2*number2,"THB")
 elif  product==4:
  rates2=49
  print("Total:",product," = ",rates2*number2,"THB")
 elif  product==5:
  rates2=30
  print("Total:",product," = ",rates2*number2,"THB")
 product=int(input("Do you want to buy? "))

 if    product==1:
  rates3=39
  print("Your product:",product," = ",rates3,"THB")
 elif  product==2:
  rates3=69
  print("Your product:",product," = ",rates3,"THB")
 elif  product==3:
  rates3=59
  print("Your product:",product," = ",rates3,"THB")
 elif  product==4:
  rates3=49
  print("Your product:",product," = ",rates3,"THB")
 elif  product==5:
  rates3=30
  print("Your product:",product," = ",rates3,"THB")
 number3=int(input("Do you want to number?"))
    
 if    product==1:
  rates3=39
  print("Total:",product," = ",rates3*number3,"THB")
 elif  product==2:
  rates=69
  print("Total:",product," = ",rates3*number3,"THB")
 elif  product==3:
  rates=59
  print("Total:",product," = ",rates3*number3,"THB")
 elif  product==4:
  rates=49
  print("Total:",product," = ",rates3*number3,"THB")
 elif  product==5:
  rates=30
  print("Total:",product," = ",rates3*number3,"THB")
 print("All Total=",rates1*number1+rates2*number2+rates3*number3,"THB")
else:
 print("Error")
