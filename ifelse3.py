# write a program that check a year is leap year or not

year = int(input("enter a year : "))

ans = year%4
# print(ans)

if ans==0:
      print("leap year : ",year)
      
else:
      print("normal year : ",year)