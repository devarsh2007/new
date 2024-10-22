name = input("enter file name : ")

obj = open(name)

# print(obj)

v = ["a","i","e","o","u"]
vowels = 0
# count = 0
for i in obj:
    for j in i:
        # count += 1
        if j in v:
            vowels+=1
        
# print("total character : ",count)
print("vowels : ",vowels)
