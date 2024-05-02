a=int(input("enter number 1 : "))
b=int(input("enter number 2 : "))

print(id(a))
print(id(b))

ans = a is b
print("is same location: ",ans)