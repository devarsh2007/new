file = open("python.txt",'w')
file.write("line 1 \n line 2 \n line 3")
file.close()

obj = open("new.txt",'a')
obj.write("12345")
file.close()

obj = open("new.txt",'a')
obj.write("\n67890")
file.close()

p1= open("python.txt",'a')
p1.write("\nhello world")
p1.close()