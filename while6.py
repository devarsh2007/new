# write a program that take input in range and print it

total = int(input("enter total number of entry : "))

entries = []

# l1=[1,2,3,4,5]
count=1
while count<=total:
      count+=1
      entry = input("enter a entry : ")
      entries.append(entry)
      
print(entries)
# print(entries[0])
number=0
while number<total:
      print(entries[number])
      number+=1