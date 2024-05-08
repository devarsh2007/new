# write a program that take input of month and print number of days 

month = int(input("enter a month : "))

if month>12 or month<1:
      print("invalid input")
      
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
      print("it has 31 days")
      
elif month==2:
      print("it has 28-29 days")
      
else:
      print("it has 30 days")