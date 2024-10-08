try:
    a=int(input("enter element : "))
    b=int(input("enter element : "))
    c=int(input("enter element : "))

    numbers = [a,b,c]

    for i in range(0,5):
        print(numbers[i])
        
except(IndexError):
    print("error")
    
finally:
    print("program end...")