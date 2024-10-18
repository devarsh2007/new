# import module1
# it import all code in module 1 file
# module1.hello()

# from module1 import calculator,hello
from module1 import *

a=int(input("enter num1 : "))
b=int(input("enter num2 : "))
obj = calculator(a,b)

obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()

hello()

n = 10
def greet():
    global n #local
    n=20
    print(n)
    
greet()