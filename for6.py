# hello
# {h:1,e:2,l:3,l:4,o:5}
# h 
# e 
# l 
# l 
# o

name = input("enter a message : ")

d1={}
count=1

# print(len(name))
for i in range(0,len(name)):
      # print(name[i])
      d1[name[i]] = count
      count+=1
      
print(d1)
