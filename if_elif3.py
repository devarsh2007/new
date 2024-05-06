# write a program that perform opration like calc

print("-"*50)
print("enter 1 for addition ")
print("enter 2 for substraction ")
print("enter 3 for multiplication ")
print("enter 4 for division ")
print("-"*50)

choise = int(input("enter your choise : "))

if choise==1 or choise==2 or choise==3 or choise==4:
      a=int(input("enter number1 : "))
      b=int(input("enter number2 : "))

if choise==1:
      print("addition : ",a+b)
      
elif choise==2:
      print("substraction : ",a-b)
      
elif choise==3:
      print("multiplication : ",a*b)
      
# else:
#       print("division")

elif choise==4:
      print("division : ",a/b)
      
else:
      print("invallid input")