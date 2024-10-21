name = input("enter file name : ")

obj = open(name)
# print(obj)

count = 0
for i in obj:
    for j in i:
        count += 1
        
print("total character : ",count)