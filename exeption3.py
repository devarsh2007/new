try:
    a=int(input("enter a : "))
    b=int(input("enter b : "))

    print(a+b)
    print((str(a)+b))
    
except ValueError:
    print("enter value in number")
    
except TypeError:
    print("this is type error...")
    
print("program end!!!")