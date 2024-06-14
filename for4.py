l1=[]
number = int(input("enter a number : "))
count=1
for i in range(0,number):
      name = input(f"enter value {count} : ")
      count+=1
      l1.append(name)
      
print(l1)