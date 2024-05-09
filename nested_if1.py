# nested if
# when one condition ocurs in other condition it becomes nested if

# write a program that find minimum number of given three numbers

a=int(input("enter first number : "))
b=int(input("enter second number : "))
c=int(input("enter third number : "))

if a<b:
      if a<c:
            print("min : ",a)
            
if b<a:
      if b<c:
            print("min : ",b)
            
if c<a:
      if c<b:
            print("min : ",c)
            
if a==c:
      if b==c:
            print("all are same")