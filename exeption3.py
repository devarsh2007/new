try:
      a=int(input("enter number1 : "))
      b=int(input("enter number2 : "))

      print(a/b)
      
except ValueError:
      print("invalid input")
      
except ZeroDivisionError:
      print("number is not divisible by 0")
      
except:
      print("error occured")
      
print("good bye")