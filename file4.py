file = open("python.txt")
data = file.read()
print("data copied...")
# print(data)
newobj = open("new.txt",'a')
# newobj.write("\n")
data = "\n"+data
newobj.write(data)
print("data paste...")

file.close()
newobj.close()