try:
    a=int(input("enter number1 : "))
    b=int(input("enter number2 : "))
    
except Exception as e:
    print("some error ocured...")
    print(e)

else:
    ans = a+b
    print(ans)

print("hello world....")