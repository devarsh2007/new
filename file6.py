import os
# os.rename("python.txt","python2.txt")
# os.rename("new.txt","new.py")

# os.remove("new.txt")

# os.mkdir("myfolder")

# os.chdir("myfolder")
print(os.getcwd())

os.chdir("../")
print(os.getcwd())

os.chdir("../py8")
print(os.getcwd())

os.chdir("../py19/baker-1.0.0/baker-1.0.0/baker-1.0.0/css")
print(os.getcwd())

os.chdir("../../../../../py3")
os.chdir("../python")
print(os.getcwd())
obj = open("file1.py","r")
for i in obj:
    print(i)
obj.close()

# os.rmdir("myfolder")