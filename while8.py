a=input("enter message : ")

name = {}
l1=[]

t1=()
t1=list(t1)

name=set(name)

last = len(a)-1
while last>=0:
      print(a[last])
      name.add(a[last])
      l1.append(a[last])
      t1.append(a[last])

      last-=1

t1=tuple(t1)

print("set : ",name)
print("list : ",l1)
print("tuple : ",t1)