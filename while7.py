# write a program that take input in range and print it

total = int(input("enter total number of entry : "))

entries = []

# l1=[1,2,3,4,5]
count=1
while count<=total:
      count+=1
      entry = input("enter a entry : ")
      entries.append(entry)
      
print("main list : ",entries)
# print(entries[0])

last=total-1
# print(last)

l2=[]
while last>=0:
      # print(entries[last])
      l2.append(entries[last])
      last-=1
      
print("reverse list : ",l2)