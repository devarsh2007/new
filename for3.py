number = int(input("enter a number : "))
l1 = []

if number>0:
      for i in range(number+1):
            # print(i)
            l1.append(i)
            
else:
      for i in range(0,number-1,-1):
            # print(i)
            l1.append(i)
            
print(l1)
